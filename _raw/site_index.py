#!/usr/bin/env python3
"""
Structural site indexer for coveredca.com  (DOM-based, standard library only).

WHY THIS EXISTS
---------------
The original PowerShell extractor flattened tables into an unordered bag of
cell contents and DISCARDED row titles. That defect caused a real error: a
6-row deadline table was rewritten as a 5-row table with invented row labels,
and the row "Birth, adoption or foster placement" was merged away, silently
transferring its coverage-start rule to a different row.

The verification pass then inherited the same extractor, so it could not see
what the writer could not see -- two layers of the same blind spot is not
verification.

This indexer captures STRUCTURE:
  * real <table> grids with every cell kept aligned to its row
  * card groups: <section>/<ul> holding <article> cards (this site presents
    several comparison blocks, e.g. "What Counts as Income", this way)
  * headings h1..h4 in document order
  * list items and FAQ-style question blocks
  * metadata

Implementation note: a small DOM tree is built first, then walked. The earlier
state-machine parser was too fragile (it missed <article> cards whose heading
was an <h3> inside a grid <ul>).

Usage:
    python site_index.py                    # index every URL in urls_en.txt
    python site_index.py --urls <u> [<u>]   # index specific URLs
"""

import json
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from html import unescape

HERE = os.path.dirname(os.path.abspath(__file__))
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")
SKIP = {"script", "style", "noscript", "svg", "path", "template", "iframe"}
BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br", "div",
         "section", "article", "tr", "td", "th", "ul", "ol"}
NOISE = re.compile(
    r"^(lucide|text-|bg-|min-|max-|w-|h-|flex|grid|rounded|relative|absolute|"
    r"container|page-|col-|sr-only|inline-|border|gap-|space-|font-|leading-|"
    r"tracking|items-|justify|overflow|z-\d|top-|left-|right-|bottom-|block|"
    r"hidden|prose|absolute|display-|heading-|label-|body-md|body-lg|body-sm)")


class Node:
    __slots__ = ("tag", "attrs", "kids", "text")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.kids = []
        self.text = []

    def iter(self):
        yield self
        for k in self.kids:
            yield from k.iter()

    def own_text(self):
        return re.sub(r"\s+", " ", "".join(self.text)).strip()


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("br", "img", "hr", "input", "meta", "link"):
            return
        n = Node(tag, dict(attrs))
        self.cur.kids.append(n)
        self.cur = n

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        # pop back to the nearest matching open tag
        stack = []
        node = self.cur
        while node is not None and node.tag != tag:
            stack.append(node)
            node = node.parent if hasattr(node, "parent") else None
        # walk up via a recorded chain instead
        if node is not None and node.tag == tag:
            newcur = self.root
            for child in self.root.kids:
                pass
        # simpler & safe: use the stack we maintain
        self._close(tag)

    # explicit parent tracking avoids fragile search
    def _close(self, tag):
        chain = []
        node = self.cur
        while node is not None:
            chain.append(node)
            node = getattr(node, "_parent", None)
        for i, n in enumerate(chain):
            if n.tag == tag:
                parent = chain[i - 1] if i > 0 else self.root
                n._parent = parent
                self.cur = parent
                return

    def handle_data(self, data):
        if self.skip:
            return
        self.cur.text.append(data)


class Builder2(HTMLParser):
    """Builder with an explicit parent stack (correct, unlike Builder)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]
        self.skip = 0

    @property
    def cur(self):
        return self.stack[-1]

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("br", "img", "hr", "input", "meta", "link"):
            return
        n = Node(tag, dict(attrs))
        self.cur.kids.append(n)
        self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.skip:
            return
        self.cur.text.append(data)


def text_of(n):
    """Full descendant text, whitespace-normalised."""
    parts = []
    for x in n.iter():
        if x.text:
            parts.append("".join(x.text))
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def clean(t):
    if not t:
        return None
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) < 2 or NOISE.match(t):
        return None
    return t


def collect_tables(root):
    out = []
    for tbl in root.iter():
        if tbl.tag != "table":
            continue
        rows = []
        # React SSR nests rows in <tbody>, so walk descendants, not direct kids
        for tr in tbl.iter():
            if tr.tag != "tr":
                continue
            cells = []
            for td in tr.iter():
                if td.tag in ("td", "th"):
                    cells.append(text_of(td))
            if any(c.strip() for c in cells):
                rows.append(cells)
        if not rows:
            continue
        header = []
        body = rows
        first = rows[0]
        if all(re.fullmatch(r"\s*", c) or len(c) < 40 for c in first) \
                and any(len(c) <= 30 for c in first):
            header, body = first, rows[1:]
        if not header:
            header, body = [], rows
        out.append({
            "header": header,
            "rows": body,
            "n_rows": len(body),
            "n_cols": max(len(r) for r in rows),
        })
    return out


def collect_headings(root):
    hs = []
    for n in root.iter():
        if n.tag in ("h1", "h2", "h3", "h4"):
            t = clean(text_of(n))
            if t:
                hs.append([n.tag, t])
    return hs


def collect_cards(root):
    """
    Capture card-based comparison blocks.

    A 'card group' is a <section> or <ul> whose <li> children contain
    <article>. Each article's first heading becomes its label and its list
    items become its values. This is how coveredca.com presents blocks such
    as "What Counts as Income" with 'Counts' / "Doesn't Count" columns.
    """
    groups = []

    def article_items(art):
        items = []
        for x in art.iter():
            if x.tag == "li":
                if any(y.tag == "article" for y in x.iter()):
                    continue                      # wrapper li, not a real item
                t = clean(text_of(x))
                if t and t not in items:
                    items.append(t)
        if not items:
            for x in art.iter():
                if x.tag == "p":
                    t = clean(text_of(x))
                    if t and t not in items:
                        items.append(t)
        # drop container artefacts: any string that merely concatenates others
        items = [t for t in items
                 if not any(t != o and o in t for o in items)]
        return items

    def art_label(art):
        # heading is usually nested inside a wrapper div, so search descendants
        for x in art.iter():
            if x.tag in ("h1", "h2", "h3", "h4"):
                t = clean(text_of(x))
                if t:
                    return t
        return ""

    def section_title(node):
        """Nearest preceding section/heading context for the group."""
        # walk previous siblings of ancestors for a heading
        for x in node.iter():
            if x.tag == "h2":
                return clean(text_of(x)) or ""
        return ""

    seen = set()
    for sec in root.iter():
        if sec.tag not in ("section", "ul", "div"):
            continue
        arts = [x for x in sec.kids
                if x.tag == "li" for y in x.kids if y.tag == "article"]
        if not arts:
            arts = [y for x in sec.kids if x.tag in ("li", "article")
                    for y in x.kids if y.tag == "article"]
        if not arts:
            continue
        cards = []
        for a in arts:
            label = art_label(a)
            items = article_items(a)
            if label or items:
                cards.append({"label": label, "items": items})
        if len(cards) < 2:
            continue
        key = tuple((c["label"], tuple(c["items"])) for c in cards)
        if key in seen:
            continue
        seen.add(key)
        groups.append({"group": section_title(sec), "cards": cards})
    return groups


def collect_faq(root):
    out = []
    for n in root.iter():
        if n.tag == "button":
            t = clean(text_of(n))
            if t and len(t) > 12 and not t.lower().startswith(("skip", "close")):
                out.append(t)
    if not out:
        for n in root.iter():
            if n.tag == "summary":
                t = clean(text_of(n))
                if t:
                    out.append(t)
    seen, res = set(), []
    for t in out:
        if t not in seen:
            seen.add(t)
            res.append(t)
    return res[:250]


def fetch(url, timeout=90, retries=3):
    last = None
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace"), r.status
        except Exception as e:                       # noqa: BLE001
            last = e
            time.sleep(1.5 * (a + 1))
    raise last


def index_page(url):
    rec = {"url": url, "ok": False, "status": None, "error": None,
           "title": "", "description": "", "bytes": 0,
           "headings": [], "tables": [], "cards": [], "faq": []}
    try:
        html, status = fetch(url)
    except Exception as e:                            # noqa: BLE001
        rec["error"] = f"{type(e).__name__}: {e}"
        return rec
    rec["ok"] = True
    rec["status"] = status
    rec["bytes"] = len(html)

    m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html)
    if m:
        rec["description"] = unescape(m.group(1))[:400]
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    if t:
        rec["title"] = re.sub(r"\s+", " ", unescape(t.group(1))).strip()[:200]

    b = Builder2()
    try:
        b.feed(html)
    except Exception as e:                            # noqa: BLE001
        rec["error"] = f"parse: {type(e).__name__}: {e}"
        return rec

    rec["headings"] = collect_headings(b.root)
    rec["tables"] = collect_tables(b.root)
    rec["cards"] = collect_cards(b.root)
    rec["faq"] = collect_faq(b.root)
    return rec


def main():
    args = sys.argv[1:]
    urls = []
    if "--urls" in args:
        urls = args[args.index("--urls") + 1:]
    else:
        with open(os.path.join(HERE, "urls_en.txt"), encoding="utf-8") as f:
            urls = [l.strip() for l in f if l.strip()]

    out = []
    for n, u in enumerate(urls, 1):
        rec = index_page(u)
        out.append(rec)
        mark = "ok " if rec["ok"] else "ERR"
        print(f"[{n:3}/{len(urls)}] {mark} tbl={len(rec['tables'])} "
              f"cards={len(rec['cards'])} h={len(rec['headings'])} "
              f"faq={len(rec['faq'])} {u}", flush=True)
        time.sleep(0.35)

    dest = os.path.join(HERE, "SITE-INDEX.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    ok = sum(1 for r in out if r["ok"])
    print(f"\nwrote {dest}")
    print(f"fetched {ok}/{len(out)}")
    print(f"pages with real <table> : {sum(1 for r in out if r['tables'])}")
    print(f"pages with card groups  : {sum(1 for r in out if r['cards'])}")
    print(f"pages with FAQ items    : {sum(1 for r in out if r['faq'])}")


if __name__ == "__main__":
    main()