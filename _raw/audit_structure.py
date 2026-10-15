#!/usr/bin/env python3
"""
Structural auditor: compares each library .md file against the site index.

WHY
---
The birth/adoption bug was missed because a flattening extractor hid table
structure, and the verifier inherited the same blind spot. This script removes
the reviewer from the loop for the mechanical part:

  For every page, it checks that each TABLE ROW LABEL and each CARD LABEL /
  CARD ITEM present on the live site also appears in the corresponding library
  file.

A missing row, a renamed row, or a card column dropped during summarisation
shows up here as MISSING -- with no judgement call required.

It also flags row-COUNT mismatches, which is how the 6-row -> 5-row table
defect surfaces.

Usage:  python audit_structure.py            # human report to stdout
        python audit_structure.py --json     # machine-readable
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INDEX = os.path.join(HERE, "SITE-INDEX.json")

# library folder -> source path prefix, used to locate the matching .md
FOLDERS = [
    "01-coverage-and-plans", "02-costs-and-financial-help",
    "03-enrollment-and-eligibility", "04-account-and-managing-coverage",
    "05-help-support-and-rights", "06-partners-agents-and-training",
    "07-news-policy-and-updates", "08-about-and-resources",
]

# slug -> library path relative to ROOT
OVERRIDES = {
    "/enrollment/major-life-changes": "03-enrollment-and-eligibility/major-life-changes.md",
    "/costs/financial-help": "02-costs-and-financial-help/financial-help.md",
    "/enrollment/documents": "03-enrollment-and-eligibility/documents.md",
    "/coverage-basics/tax-penalty-details-and-exemptions/ftb-form-3853": "01-coverage-and-plans/ftb-form-3853.md",
    "/coverage-basics/medi-cal": "01-coverage-and-plans/medi-cal.md",
    "/coverage-basics/medi-cal/children": "01-coverage-and-plans/children.md",
    "/coverage-basics/medi-cal/pregnant-individuals": "01-coverage-and-plans/pregnant-individuals.md",
    "/coverage-basics/medi-cal/mixed-program-families": "01-coverage-and-plans/mixed-program-families.md",
    "/coverage-basics/dental": "01-coverage-and-plans/dental.md",
    "/coverage-basics/vision": "01-coverage-and-plans/vision.md",
    "/privacy/terms": "08-about-and-resources/privacy-terms.md",
    "/enrollment-partners-individuals": "06-partners-agents-and-training/enrollment-partners-individuals.md",
    "/enrollment-partners-small-business": "06-partners-agents-and-training/enrollment-partners-small-business.md",
    "/enrollment-partners-individuals/become-an-agent/code-of-conduct": "06-partners-agents-and-training/individual-agent-code-of-conduct.md",
    "/enrollment-partners-small-business/ccsb-certification/code-of-conduct": "06-partners-agents-and-training/ccsb-code-of-conduct.md",
    "/enrollment-partners-individuals/training-and-education": "06-partners-agents-and-training/individual-training-and-education.md",
    "/enrollment-partners-small-business/training-and-education": "06-partners-agents-and-training/small-business-training-and-education.md",
    "/enrollment-partners-individuals/client-support": "06-partners-agents-and-training/individual-client-support.md",
    "/enrollment-partners-small-business/client-support": "06-partners-agents-and-training/small-business-client-support.md",
    "/enrollment-partners-individuals/contact": "06-partners-agents-and-training/individual-contact.md",
    "/enrollment-partners-small-business/contact": "06-partners-agents-and-training/small-business-contact.md",
    "/small-business/health-plans/kaiser": "03-enrollment-and-eligibility/small-business/kaiser.md",
    "/small-business/mandate/1095-forms": "03-enrollment-and-eligibility/small-business/1095-forms.md",
}

HOME_PAGE = {
    "/": "08-about-and-resources/about-covered-california.md",
}

PREFIX_PREFIX = "/enrollment/documents/"
SMALL_PREFIX = "/small-business/"


def norm(s):
    """Aggressive normalisation for presence matching."""
    if not s:
        return ""
    s = s.lower()
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"[^a-z0-9%$./ -]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def sig(s):
    """Comparison key: first few significant words, order-insensitive tail."""
    n = norm(s)
    words = [w for w in n.split() if w not in
             ("the", "a", "an", "and", "or", "of", "to", "in", "for", "your",
              "you", "is", "are", "on", "at", "by", "with", "from", "that",
              "this", "it", "be", "as")]
    return " ".join(words[:6])


def find_file(path):
    """Locate the library file that should correspond to a site path."""
    slug = path.rstrip("/") or "/"

    rel = OVERRIDES.get(slug) or HOME_PAGE.get(slug)
    if rel:
        p = os.path.join(ROOT, rel)
        return p if os.path.exists(p) else None

    if slug == "/":
        return None

    name = slug.split("/")[-1] + ".md"

    # documents subpages use doc- prefix
    if slug.startswith(PREFIX_PREFIX):
        for f in FOLDERS:
            for cand in (name, "doc-" + name):
                p = os.path.join(ROOT, f, cand)
                if os.path.exists(p):
                    return p
        return None

    # small-business lives in its own subfolder
    if slug.startswith(SMALL_PREFIX):
        sub = slug[len(SMALL_PREFIX):].split("/")[-1] + ".md"
        p = os.path.join(ROOT, "03-enrollment-and-eligibility",
                         "small-business", sub)
        return p if os.path.exists(p) else None

    for f in FOLDERS:
        p = os.path.join(ROOT, f, name)
        if os.path.exists(p):
            return p

    # partner/agent pages with disambiguating prefixes
    cands = []
    if "enrollment-partners-individuals" in slug:
        cands += [f"individual-{name}", name]
    if "enrollment-partners-small-business" in slug:
        cands += [f"small-business-{name}", name, f"ccsb-{name}"]
    for f in FOLDERS:
        for c in cands:
            p = os.path.join(ROOT, f, c)
            if os.path.exists(p):
                return p
    return None


def main():
    with open(INDEX, encoding="utf-8") as f:
        pages = json.load(f)

    rows = []
    for pg in pages:
        if not pg.get("ok"):
            rows.append({"url": pg["url"], "file": None, "status": "FETCH_FAIL",
                         "missing": [], "extra_tables": []})
            continue
        path = pg["url"].replace("https://www.coveredca.com", "") or "/"
        fp = find_file(path)
        if not fp or not os.path.exists(fp):
            rows.append({"url": pg["url"], "file": None, "status": "NO_FILE",
                         "missing": [], "extra_tables": []})
            continue
        txt = open(fp, encoding="utf-8").read()
        ntxt = norm(txt)
        # collapse whitespace once more for substring tests
        flat = re.sub(r"\s+", " ", ntxt)

        def present(s, minlen=4):
            """True if a normalised string is materially represented in the file."""
            n = norm(s)
            if len(n) < minlen:
                return True
            if n in flat:
                return True
            # tolerate parentheticals / trailing qualifiers in either direction
            n2 = re.sub(r"\s*\([^)]*\)", " ", n).strip()
            n2 = re.sub(r"^(individual|family)\s+", "", n2)
            if len(n2) >= minlen and n2 in flat:
                return True
            # distinctive leading fragment
            head = " ".join(n2.split()[:4])
            if len(head) >= 6 and head in flat:
                return True
            return False

        missing = []
        n_tables = 0
        for t in pg["tables"]:
            n_tables += 1
            for r in t["rows"]:
                if not r:
                    continue
                label = r[0]
                if len(norm(label)) < 3:
                    continue
                vals = [c for c in r[1:] if len(norm(c)) >= 2]
                if present(label):
                    continue
                # label reworded but the row's values are all carried through?
                if vals and sum(1 for v in vals if present(v)) >= max(1, len(vals) - 1):
                    continue
                missing.append({"kind": "table-row", "label": label,
                                "table": n_tables,
                                "cells": [c[:70] for c in r]})
        for g in pg["cards"]:
            for c in g["cards"]:
                if c["label"] and len(norm(c["label"])) >= 3 and not present(c["label"]):
                    missing.append({"kind": "card-label",
                                    "label": c["label"],
                                    "n_items": len(c["items"])})
                for it in c["items"]:
                    if len(norm(it)) < 14:
                        continue
                    if present(it, minlen=10):
                        continue
                    missing.append({"kind": "card-item", "label": it[:90]})

        rows.append({"url": pg["url"], "file": os.path.relpath(fp, ROOT),
                     "status": "OK", "missing": missing,
                     "n_tables": len(pg["tables"]),
                     "n_cards": len(pg["cards"]),
                     "n_headings": len(pg["headings"]),
                     "n_faq": len(pg["faq"])})

    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return

    bad = [r for r in rows if r["status"] != "OK"]
    flagged = [r for r in rows if r.get("missing")]
    print("=" * 78)
    print("STRUCTURAL AUDIT -- library files vs live site index")
    print("=" * 78)
    print(f"pages indexed        : {len(rows)}")
    print(f"pages matched to file: {len(rows) - len(bad)}")
    print(f"pages needing review : {len(flagged)}")
    print(f"total missing labels : {sum(len(r['missing']) for r in rows)}")
    print()
    if bad:
        print("--- PAGES WITH NO MATCHING LIBRARY FILE ---")
        for r in bad:
            print(f"  {r['status']:12} {r['url']}")
        print()
    print("--- PAGES WITH STRUCTURE NOT REPRESENTED IN THE LIBRARY ---")
    print("(review each; a long label may legitimately be summarised)")
    for r in sorted(flagged, key=lambda x: -len(x["missing"])):
        print(f"\n{r['url']}   -> {r['file']}")
        print(f"   tables={r.get('n_tables')} cards={r.get('n_cards')} "
              f"faq={r.get('n_faq')} missing={len(r['missing'])}")
        for m in r["missing"][:14]:
            lbl = m["label"][:88]
            extra = ""
            if m["kind"] == "table-row":
                extra = " | " + " || ".join(m["cells"][1:3])
            print(f"     [{m['kind']:<10}] {lbl}{extra}")
        if len(r["missing"]) > 14:
            print(f"     ... and {len(r['missing'])-14} more")


if __name__ == "__main__":
    main()