#!/usr/bin/env python3
"""Write one office-life joke to /output/entry.txt.

Competition: Make the AI Judge Laugh (u-alfasurya91-make-the-ai-judge-laugh-6ed40225).
Judge brief, in order: (1) about office life, lands as a joke; (2) true
observation (meetings, email, bosses, coffee, deadlines, printer);
(3) surprising turn, fresh angle, unexpected last word, not a pun or stock
line; (4) tight, one line, no wasted setup, reads cleanly aloud;
(5) original, not a familiar line with nouns swapped.

Entry shape (per RANK-UP.md): ONE concrete scene + ONE reversal + ONE
landing final line. Scene: a meeting where nobody understands the plan.
Reversal: everyone nods anyway. Landing: the nodding itself creates the
deadline. Fresh angle: the joke is not about the meeting being useless
(saturated) but about collective pretending manufacturing a deadline.
"""
import os
import sys

ENTRY = "Nobody in the meeting understood the plan, but everyone nodded, so now it's a deadline."
MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the entry is valid."""
    if not text or not text.strip():
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 200-char limit" % len(text)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(c) < 32 for c in text):
        return "entry contains a control character"
    return None


def main():
    err = validate(ENTRY)
    if err:
        print("invalid entry: %s" % err, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to /output/entry.txt" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
