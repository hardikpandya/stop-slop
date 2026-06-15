#!/usr/bin/env python3
"""
stop-slop analyze: Interactive AI-writing pattern detector.

Usage:
    python3 analyze.py <file.txt>
    echo "your text" | python3 analyze.py
    python3 analyze.py --interactive

Scans text against patterns from phrases.md and structures.md,
highlights detected AI-writing signals, and produces a slop score.
"""

import sys
import re
import os
import json
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent


def load_patterns():
    """Load all pattern definitions from reference files."""
    patterns = {
        "throat_clearing": [],
        "emphasis_crutches": [],
        "business_jargon": {},
        "adverbs": [],
        "filler_phrases": [],
        "meta_commentary": [],
        "performative_emphasis": [],
        "telling_not_showing": [],
        "vague_declaratives": [],
        "binary_contrasts": [],
        "negative_listing": [],
        "dramatic_fragmentation": [],
        "rhetorical_setups": [],
        "false_agency": [],
        "narrator_distance": [],
        "passive_voice": [],
        "sentence_starters": [],
        "rhythm_patterns": [],
        "lazy_extremes": [],
    }

    # --- Parse phrases.md ---
    phrases_file = SKILL_DIR / "references" / "phrases.md"
    if phrases_file.exists():
        content = phrases_file.read_text()
        current_section = None

        for line in content.splitlines():
            stripped = line.strip()

            # Detect section headers
            if stripped.startswith("## "):
                header = stripped[3:].lower()
                if "throat" in header:
                    current_section = "throat_clearing"
                elif "emphasis crutch" in header:
                    current_section = "emphasis_crutches"
                elif "business jargon" in header:
                    current_section = "business_jargon_header"
                elif "adverb" in header:
                    current_section = "adverbs"
                elif "filler" in header:
                    current_section = "filler_phrases"
                elif "meta" in header:
                    current_section = "meta_commentary"
                elif "performative" in header:
                    current_section = "performative_emphasis"
                elif "telling" in header:
                    current_section = "telling_not_showing"
                elif "vague" in header:
                    current_section = "vague_declaratives"
                else:
                    current_section = None
                continue

            # Parse list items
            if stripped.startswith("- "):
                item = stripped[2:].strip().strip('"').strip()

                if current_section == "throat_clearing":
                    patterns["throat_clearing"].append(item)
                elif current_section == "emphasis_crutches":
                    patterns["emphasis_crutches"].append(item)
                elif current_section == "adverbs":
                    patterns["adverbs"].append(item)
                elif current_section == "filler_phrases":
                    patterns["filler_phrases"].append(item)
                elif current_section == "meta_commentary":
                    patterns["meta_commentary"].append(item)
                elif current_section == "performative_emphasis":
                    patterns["performative_emphasis"].append(item)
                elif current_section == "telling_not_showing":
                    patterns["telling_not_showing"].append(item)
                elif current_section == "vague_declaratives":
                    patterns["vague_declaratives"].append(item)

            # Parse business jargon table
            if current_section == "business_jargon_header" and "|" in stripped:
                if "Avoid" in stripped or "---" in stripped:
                    continue
                parts = [p.strip() for p in stripped.split("|")]
                if len(parts) >= 3 and parts[0]:
                    patterns["business_jargon"][parts[0]] = parts[1]

    # --- Parse structures.md ---
    structures_file = SKILL_DIR / "references" / "structures.md"
    if structures_file.exists():
        content = structures_file.read_text()
        current_section = None

        for line in content.splitlines():
            stripped = line.strip()

            if stripped.startswith("## "):
                header = stripped[3:].lower()
                if "binary" in header:
                    current_section = "binary_contrasts"
                elif "negative listing" in header:
                    current_section = "negative_listing"
                elif "dramatic fragmentation" in header:
                    current_section = "dramatic_fragmentation"
                elif "rhetorical" in header:
                    current_section = "rhetorical_setups"
                elif "false agency" in header:
                    current_section = "false_agency"
                elif "narrator" in header:
                    current_section = "narrator_distance"
                elif "passive" in header:
                    current_section = "passive_voice"
                elif "sentence starter" in header:
                    current_section = "sentence_starters"
                elif "rhythm" in header:
                    current_section = "rhythm_patterns"
                elif "word pattern" in header or "lazy" in header:
                    current_section = "lazy_extremes"
                else:
                    current_section = None
                continue

            # Parse pattern tables
            if "|" in stripped and current_section and "Pattern" not in stripped and "---" not in stripped:
                parts = [p.strip() for p in stripped.split("|")]
                if len(parts) >= 2 and parts[0]:
                    pattern_text = parts[0].strip('"')
                    if current_section == "binary_contrasts":
                        patterns["binary_contrasts"].append(pattern_text)
                    elif current_section == "negative_listing":
                        patterns["negative_listing"].append(pattern_text)
                    elif current_section == "dramatic_fragmentation":
                        patterns["dramatic_fragmentation"].append(pattern_text)
                    elif current_section == "rhetorical_setups":
                        patterns["rhetorical_setups"].append(pattern_text)
                    elif current_section == "false_agency":
                        patterns["false_agency"].append(pattern_text)
                    elif current_section == "narrator_distance":
                        patterns["narrator_distance"].append(pattern_text)
                    elif current_section == "passive_voice":
                        patterns["passive_voice"].append(pattern_text)
                    elif current_section == "sentence_starters":
                        patterns["sentence_starters"].append(pattern_text)
                    elif current_section == "rhythm_patterns":
                        patterns["rhythm_patterns"].append(pattern_text)
                    elif current_section == "lazy_extremes":
                        patterns["lazy_extremes"].append(pattern_text)

    return patterns


def check_text(text, patterns):
    """Check text against all patterns. Returns list of findings."""
    findings = []
    lines = text.splitlines()

    # --- Exact/phrase matches ---
    phrase_categories = [
        ("throat_clearing", "Throat-Clearing Opener"),
        ("emphasis_crutches", "Emphasis Crutch"),
        ("adverbs", "Adverb"),
        ("filler_phrases", "Filler Phrase"),
        ("meta_commentary", "Meta-Commentary"),
        ("performative_emphasis", "Performative Emphasis"),
        ("telling_not_showing", "Telling Not Showing"),
        ("vague_declaratives", "Vague Declarative"),
        ("rhetorical_setups", "Rhetorical Setup"),
        ("false_agency", "False Agency"),
        ("narrator_distance", "Narrator from Distance"),
        ("lazy_extremes", "Lazy Extreme"),
    ]

    for key, label in phrase_categories:
        for pattern in patterns.get(key, []):
            # Build regex: handle patterns with placeholders like [X]
            escaped = re.escape(pattern)
            # Un-escape the \[ and \] so they stay as regex character classes
            regex_pattern = escaped.replace(r"\[", "[").replace(r"\]", "]")
            # Make it case-insensitive
            try:
                compiled = re.compile(regex_pattern, re.IGNORECASE)
            except re.error:
                continue

            for i, line in enumerate(lines, 1):
                match = compiled.search(line)
                if match:
                    findings.append({
                        "line": i,
                        "category": label,
                        "pattern": pattern,
                        "matched": match.group(0),
                        "context": line.strip(),
                        "suggestion": f"Remove or rewrite: '{match.group(0)}'",
                    })

    # --- Business jargon ---
    for jargon, replacement in patterns.get("business_jargon", {}).items():
        for i, line in enumerate(lines, 1):
            if re.search(r'\b' + re.escape(jargon) + r'\b', line, re.IGNORECASE):
                findings.append({
                    "line": i,
                    "category": "Business Jargon",
                    "pattern": jargon,
                    "matched": jargon,
                    "context": line.strip(),
                    "suggestion": f"Replace '{jargon}' with '{replacement}'",
                })

    # --- Passive voice detection ---
    passive_patterns = [
        r'\bwas\s+\w+ed\b',
        r'\bwere\s+\w+ed\b',
        r'\bis\s+\w+ed\b',
        r'\bare\s+\w+ed\b',
        r'\bbeen\s+\w+ed\b',
        r'\bit is believed that\b',
        r'\bit was decided that\b',
        r'\bit has been shown\b',
        r'\bmistakes were made\b',
    ]
    for pp in passive_patterns:
        compiled = re.compile(pp, re.IGNORECASE)
        for i, line in enumerate(lines, 1):
            match = compiled.search(line)
            if match:
                findings.append({
                    "line": i,
                    "category": "Passive Voice",
                    "pattern": pp,
                    "matched": match.group(0),
                    "context": line.strip(),
                    "suggestion": "Rewrite in active voice. Name the actor.",
                })

    # --- Sentence starters ---
    wh_starters = ['what ', 'when ', 'where ', 'which ', 'who ', 'why ', 'how ']
    for i, line in enumerate(lines, 1):
        stripped = line.strip().lower()
        for starter in wh_starters:
            if stripped.startswith(starter):
                findings.append({
                    "line": i,
                    "category": "Wh- Sentence Starter",
                    "pattern": starter.strip(),
                    "matched": line.strip()[:60],
                    "context": line.strip(),
                    "suggestion": "Restructure: lead with the subject or verb.",
                })
                break

    # --- Em-dash overuse ---
    for i, line in enumerate(lines, 1):
        em_dash_count = line.count('—') + line.count('--')
        if em_dash_count >= 2:
            findings.append({
                "line": i,
                "category": "Em-Dash Overuse",
                "pattern": "multiple em-dashes",
                "matched": "—" * em_dash_count,
                "context": line.strip(),
                "suggestion": "Remove em-dashes. Use commas or periods.",
            })

    # --- Staccato fragmentation (3+ consecutive very short sentences) ---
    for i in range(len(lines) - 2):
        window = lines[i:i+3]
        stripped = [l.strip() for l in window if l.strip()]
        if len(stripped) >= 3:
            avg_len = sum(len(l.split()) for l in stripped) / len(stripped)
            if avg_len <= 4:
                findings.append({
                    "line": i + 1,
                    "category": "Staccato Fragmentation",
                    "pattern": "3+ short consecutive sentences",
                    "matched": " | ".join(l.strip()[:40] for l in stripped),
                    "context": " | ".join(l.strip() for l in stripped),
                    "suggestion": "Combine or vary sentence length. Avoid manufactured drama.",
                })

    # --- Three-item lists ---
    three_item = re.compile(r'\b(\w+),\s+(\w+),\s+(?:and|or)\s+(\w+)\b', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        match = three_item.search(line)
        if match:
            findings.append({
                "line": i,
                "category": "Three-Item List",
                "pattern": "X, Y, and/or Z",
                "matched": match.group(0),
                "context": line.strip(),
                "suggestion": "Use two items or one. Three is a cliché rhythm.",
            })

    # --- Generic conclusion detection ---
    conclusion_patterns = [
        r'\bin conclusion\b',
        r'\bto sum up\b',
        r'\bin summary\b',
        r'\ball in all\b',
        r'\bat the end of the day\b',
        r'\bthe bottom line\b',
        r'\bultimately\b',
    ]
    for cp in conclusion_patterns:
        compiled = re.compile(cp, re.IGNORECASE)
        for i, line in enumerate(lines, 1):
            if compiled.search(line):
                findings.append({
                    "line": i,
                    "category": "Generic Conclusion",
                    "pattern": cp,
                    "matched": line.strip()[:60],
                    "context": line.strip(),
                    "suggestion": "State the conclusion directly. Cut the wrapper.",
                })

    # --- Repeated sentence openings ---
    openings = {}
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped:
            first_word = stripped.split()[0].lower().rstrip('.,;:') if stripped.split() else ""
            if first_word:
                openings.setdefault(first_word, []).append(i)

    for word, line_nums in openings.items():
        if len(line_nums) >= 3:
            findings.append({
                "line": line_nums[0],
                "category": "Repeated Sentence Opening",
                "pattern": f"'{word}' used {len(line_nums)} times as sentence start",
                "matched": f"Lines: {', '.join(str(n) for n in line_nums[:5])}",
                "context": f"First: {lines[line_nums[0]-1].strip()[:60]}",
                "suggestion": "Vary sentence openings. Don't start multiple sentences the same way.",
            })

    # Deduplicate: same line + category = one finding
    seen = set()
    deduped = []
    for f in findings:
        key = (f["line"], f["category"], f["matched"].lower())
        if key not in seen:
            seen.add(key)
            deduped.append(f)

    return sorted(deduped, key=lambda x: (x["line"], x["category"]))


def compute_slop_score(findings, text):
    """Compute a slop score from 0 (clean) to 100 (maximum slop)."""
    lines = [l for l in text.splitlines() if l.strip()]
    total_lines = max(len(lines), 1)

    # Weight different categories
    weights = {
        "Throat-Clearing Opener": 8,
        "Emphasis Crutch": 5,
        "Business Jargon": 6,
        "Adverb": 3,
        "Filler Phrase": 4,
        "Meta-Commentary": 7,
        "Performative Emphasis": 6,
        "Telling Not Showing": 7,
        "Vague Declarative": 8,
        "Binary Contrast": 7,
        "Negative Listing": 6,
        "Dramatic Fragmentation": 6,
        "Rhetorical Setup": 5,
        "False Agency": 7,
        "Narrator from Distance": 6,
        "Passive Voice": 5,
        "Wh- Sentence Starter": 4,
        "Em-Dash Overuse": 3,
        "Staccato Fragmentation": 5,
        "Three-Item List": 3,
        "Generic Conclusion": 5,
        "Repeated Sentence Opening": 4,
    }

    raw_score = 0
    for f in findings:
        raw_score += weights.get(f["category"], 3)

    # Normalize: cap at 100
    # Scale so that ~10 findings of average weight 5 = ~50
    score = min(100, int((raw_score / max(total_lines, 5)) * 10))
    return score


def score_dimensions(findings, text):
    """Score the 5 dimensions from SKILL.md rubric (1-10 each)."""
    categories = {f["category"] for f in findings}
    lines = [l for l in text.splitlines() if l.strip()]
    total = max(len(lines), 1)
    finding_density = len(findings) / total

    # Directness: penalize throat-clearing, meta, vague, rhetorical
    directness_damage = sum(1 for c in categories & {
        "Throat-Clearing Opener", "Meta-Commentary", "Vague Declarative",
        "Rhetorical Setup", "Generic Conclusion", "Telling Not Showing"
    })
    directness = max(1, 10 - directness_damage * 2)

    # Rhythm: penalize staccato, three-item, repeated openings, em-dash
    rhythm_damage = sum(1 for c in categories & {
        "Staccato Fragmentation", "Three-Item List", "Repeated Sentence Opening",
        "Em-Dash Overuse"
    })
    rhythm = max(1, 10 - rhythm_damage * 2)

    # Trust: penalize emphasis crutches, performative, adverbs, lazy extremes
    trust_damage = sum(1 for c in categories & {
        "Emphasis Crutch", "Performative Emphasis", "Adverb", "Lazy Extreme",
        "Filler Phrase"
    })
    trust = max(1, 10 - trust_damage * 1)

    # Authenticity: penalize business jargon, false agency, narrator distance
    authenticity_damage = sum(1 for c in categories & {
        "Business Jargon", "False Agency", "Narrator from Distance",
        "Dramatic Fragmentation"
    })
    authenticity = max(1, 10 - authenticity_damage * 2)

    # Density: based on overall finding density
    density = max(1, 10 - int(finding_density * 20))

    return {
        "Directness": directness,
        "Rhythm": rhythm,
        "Trust": trust,
        "Authenticity": authenticity,
        "Density": density,
    }


def format_report(findings, text):
    """Format a human-readable report."""
    lines = []
    slop_score = compute_slop_score(findings, text)
    dimensions = score_dimensions(findings, text)
    dim_total = sum(dimensions.values())

    lines.append("=" * 60)
    lines.append("  STOP SLOP — AI Writing Pattern Analysis")
    lines.append("=" * 60)
    lines.append("")

    # Summary
    lines.append(f"  Findings: {len(findings)} issues detected")
    lines.append(f"  Slop Score: {slop_score}/100  ({'CLEAN' if slop_score < 20 else 'MODERATE' if slop_score < 50 else 'HEAVY' if slop_score < 80 else 'SEVERE'})")
    lines.append("")

    # Dimension scores
    lines.append("  Dimension Scores:")
    lines.append("  " + "-" * 40)
    for dim, score in dimensions.items():
        bar = "█" * score + "░" * (10 - score)
        lines.append(f"    {dim:<15} {bar} {score}/10")
    lines.append(f"    {'TOTAL':<15} {'':>11} {dim_total}/50")
    lines.append("")

    if dim_total < 35:
        lines.append("  ⚠  Score below 35/50 — revision recommended.")
    else:
        lines.append("  ✓  Score above 35/50 — acceptable range.")
    lines.append("")

    if not findings:
        lines.append("  No AI-writing patterns detected. Looks clean!")
        lines.append("")
        return "\n".join(lines)

    # Group findings by category
    by_category = {}
    for f in findings:
        by_category.setdefault(f["category"], []).append(f)

    lines.append("  Detected Patterns:")
    lines.append("  " + "-" * 40)

    for category, items in sorted(by_category.items()):
        lines.append(f"\n  [{category}] — {len(items)} occurrence(s)")
        for item in items:
            lines.append(f"    Line {item['line']}: \"{item['matched']}\"")
            # Truncate long context
            ctx = item['context'][:80] + "..." if len(item['context']) > 80 else item['context']
            lines.append(f"      Context: {ctx}")
            lines.append(f"      → {item['suggestion']}")

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)


def main():
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)

    if "--json" in args:
        args.remove("--json")
        output_json = True
    else:
        output_json = False

    # Load patterns
    patterns = load_patterns()

    # Get input text
    if "--interactive" in args:
        print("Paste your text (Ctrl+D when done):")
        text = sys.stdin.read()
    elif args:
        # Read from file
        filepath = args[0]
        if not os.path.exists(filepath):
            print(f"Error: file not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        text = open(filepath).read()
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print("Usage: analyze.py <file.txt>  OR  echo 'text' | analyze.py")
            print("       analyze.py --interactive")
            sys.exit(1)
        text = sys.stdin.read()

    if not text.strip():
        print("No text provided.", file=sys.stderr)
        sys.exit(1)

    findings = check_text(text, patterns)

    if output_json:
        slop_score = compute_slop_score(findings, text)
        dimensions = score_dimensions(findings, text)
        result = {
            "slop_score": slop_score,
            "dimensions": dimensions,
            "dimension_total": sum(dimensions.values()),
            "findings_count": len(findings),
            "findings": findings,
        }
        print(json.dumps(result, indent=2))
    else:
        print(format_report(findings, text))


if __name__ == "__main__":
    main()
