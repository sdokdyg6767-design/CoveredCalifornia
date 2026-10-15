#!/usr/bin/env python3
"""Print the structural record for one page from SITE-INDEX.json.

    python show_page.py major-life-changes
    python show_page.py coverage-levels/silver
    python show_page.py --list tables      # pages containing real tables
    python show_page.py --list cards       # pages containing card groups
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = json.load(open(os.path.join(HERE, "SITE-INDEX.json"), encoding="utf-8"))


def show(p):
    s = p["url"].replace("https://www.coveredca.com", "") or "/"
    print("=" * 78)
    print(f"{s}")
    print(f"{p.get('title','')} — {p.get('bytes',0):,} bytes")
    print("=" * 78)
    if not p.get("ok"):
        print("FETCH FAILED:", p.get("error"))
        return
    print(f"headings={len(p['headings'])} tables={len(p['tables'])} "
          f"cards={len(p['cards'])} faq={len(p['faq'])}")
    if p["headings"]:
        print("\n-- HEADINGS --")
        for lvl, t in p["headings"]:
            print(f"  {lvl}: {t}")
    for ti, t in enumerate(p["tables"], 1):
        print(f"\n-- TABLE {ti}: {t['n_rows']} rows x {t['n_cols']} cols --")
        if t["header"]:
            print("  | " + " | ".join(h or " " for h in t["header"]) + " |")
            print("  |" + "|".join(["---"] * len(t["header"])) + "|")
        for row in t["rows"]:
            print("  | " + " | ".join((c or "").replace("|", "\\|") for c in row) + " |")
    for gi, g in enumerate(p["cards"], 1):
        print(f"\n-- CARD GROUP {gi} --"
              + (f"  [{g['group']}]" if g.get("group") else ""))
        for c in g["cards"]:
            print(f"  * {c['label'] or '(no label)'}")
            for it in c["items"]:
                print(f"      - {it}")
    if p["faq"]:
        print(f"\n-- FAQ ({len(p['faq'])}) --")
        for q in p["faq"]:
            print(f"  - {q}")


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "--list":
        want = a[1]
        for p in PAGES:
            if not p.get("ok"):
                continue
            if want == "tables" and p["tables"]:
                s = p["url"].replace("https://www.coveredca.com", "") or "/"
                print(f"{s}  ({sum(len(t['rows']) for t in p['tables'])} rows)")
            if want == "cards" and p["cards"]:
                s = p["url"].replace("https://www.coveredca.com", "") or "/"
                print(f"{s}  ({sum(len(g['cards']) for g in p['cards'])} cards)")
        return
    key = a[0].strip("/").lower() if a else ""
    hits = [p for p in PAGES
            if key and key in p["url"].replace("https://www.coveredca.com", "").lower()]
    if not hits:
        print("no match for", a)
        print("\npages containing real tables:")
        main.__globals__  # noop
        for p in PAGES:
            if p.get("ok") and p["tables"]:
                print("  ", p["url"].replace("https://www.coveredca.com", "") or "/")
        return
    for p in hits:
        show(p)


if __name__ == "__main__":
    main()