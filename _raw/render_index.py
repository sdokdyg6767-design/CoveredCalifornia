#!/usr/bin/env python3
"""Render SITE-INDEX.json into a readable structural map (SITE-INDEX.md)."""
import json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def risk(r):
    return 6*len(r["tables"]) + 4*len(r["cards"]) + 0.02*len(r["faq"]) \
         + 0.002*max(0, r["bytes"]-300000)

def main():
    pages = json.load(open(os.path.join(HERE,"SITE-INDEX.json"),encoding="utf-8"))
    ok = [p for p in pages if p.get("ok")]
    bad = [p for p in pages if not p.get("ok")]

    out = []
    A = out.append
    A("# Covered California — Structural Site Index")
    A("")
    A("Generated 2026-10-13 by `_raw/site_index.py` from the live site.  ")
    A("This is a **structure map**, not a content summary: for every page it records the "
      "real `<table>` grids (with each cell kept aligned to its own row), the card groups, "
      "the heading outline, and the FAQ items.")
    A("")
    A("It exists because the first extractor used to build the library **flattened tables "
      "and discarded row labels**, which silently merged a row away. Anything on this site "
      "expressed as a table or card must be transcribed row-by-row, not as a bag of text.")
    A("")
    A(f"- Pages indexed: **{len(ok)}/{len(pages)}**")
    A(f"- Pages containing real `<table>` elements: **{sum(1 for p in ok if p['tables'])}** "
      f"({sum(len(p['tables']) for p in ok)} tables)")
    A(f"- Pages containing card groups: **{sum(1 for p in ok if p['cards'])}** "
      f"({sum(len(p['cards']) for p in ok)} groups)")
    A(f"- Total FAQ items captured: **{sum(len(p['faq']) for p in ok)}**")
    if bad:
        A(f"- **Failed to fetch: {len(bad)}**")
    A("")

    # ---- overview table
    A("## Risk ranking")
    A("")
    A("Pages are ordered by how likely a flattening extractor would corrupt them "
      "(tables weighted heaviest, since that is where row-to-rule mis-assignment happens).")
    A("")
    A("| # | Page | Tables | Cards | FAQ | KB |")
    A("|---:|---|---:|---:|---:|---:|")
    for i,p in enumerate(sorted(ok,key=risk,reverse=True),1):
        s = p["url"].replace("https://www.coveredca.com","") or "/"
        A(f"| {i} | `{s}` | {len(p['tables'])} | {len(p['cards'])} | "
          f"{len(p['faq'])} | {p['bytes']//1024} |")
    A("")

    # ---- per page detail
    A("## Per-page structure")
    A("")
    by_folder = defaultdict(list)
    for p in ok:
        s = p["url"].replace("https://www.coveredca.com","") or "/"
        top = s.strip("/").split("/")[0] or "(home)"
        by_folder[top].append(p)
    order = ["coverage-basics","costs","enrollment","account","get-help",
             "consumer-protection","insurance-company-contacts","ombuds-office",
             "small-business","enrollment-partners-individuals",
             "enrollment-partners-small-business","important-changes",
             "glossary","privacy","about-covered-california",
             "accessibility-and-language-support","legal-notices",
             "media-inquiries","marketing-blog",
             "social-media-commenting-disclaimer","(home)"]
    for grp in order + [g for g in by_folder if g not in order]:
        if grp not in by_folder:
            continue
        A(f"### {grp}")
        A("")
        for p in sorted(by_folder[grp], key=lambda x: x["url"]):
            s = p["url"].replace("https://www.coveredca.com","") or "/"
            A(f"#### `{s}`")
            A("")
            if p.get("title"):
                A(f"*{p['title']}* — {len(p['headings'])} headings, "
                  f"{len(p['tables'])} table(s), {len(p['cards'])} card group(s), "
                  f"{len(p['faq'])} FAQ item(s), {p['bytes']:,} bytes")
                A("")
            for ti,t in enumerate(p["tables"],1):
                A(f"**Table {ti}** — {t['n_rows']} rows x {t['n_cols']} cols")
                A("")
                if t["header"]:
                    A("| " + " | ".join(h or " " for h in t["header"]) + " |")
                    A("|" + "|".join(["---"]*len(t["header"])) + "|")
                for row in t["rows"]:
                    cells = [(c or "").replace("|","\\|") for c in row]
                    A("| " + " | ".join(cells) + " |")
                A("")
            for gi,g in enumerate(p["cards"],1):
                A(f"**Card group {gi}**" + (f" — *{g['group']}*" if g.get("group") else ""))
                A("")
                for c in g["cards"]:
                    A(f"- **{c['label'] or '(unlabelled)'}**")
                    for it in c["items"]:
                        A(f"  - {it}")
                A("")
            if p["faq"]:
                A(f"**FAQ / accordions ({len(p['faq'])})**")
                A("")
                for q in p["faq"]:
                    A(f"- {q}")
                A("")
        A("")

    dest = os.path.join(ROOT, "SITE-INDEX.md")
    open(dest,"w",encoding="utf-8").write("\n".join(out))
    print("wrote", dest, len("\n".join(out)), "chars")

if __name__ == "__main__":
    main()