#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. The brief's gate: UTF-8 text of 1 to 400 characters,
not only white space, a single line.

Concept: the entrant, as a furious judge, sentences his own office
chair — which sinks a little lower every ten minutes — for contempt
of court. One specific petty target, no throat-clearing, anger with
a precise verdict.
"""

import os
import sys

MAX_CHARS = 400

RANT = (
    "My office chair has one job \u2014 hold me at desk height \u2014 and it quits "
    "daily. I sit down a professional; ten minutes later I am a goblin folded "
    "into a question mark, knees at my chin, dignity somewhere near the floor. "
    "It sinks silently, like a coward. I have sentenced printers and one haunted "
    "photocopier, but this chair? Contempt of court. Life without parole."
)


def validate(text):
    """Check the rant against the brief's gate; return a list of problems."""
    problems = []
    if not text.strip():
        problems.append("rant is blank or only white space")
    if "\n" in text or "\r" in text:
        problems.append("rant must be a single line")
    if len(text) > MAX_CHARS:
        problems.append(
            "rant is %d characters, over the %d-character cap"
            % (len(text), MAX_CHARS)
        )
    if len(text) < 1:
        problems.append("rant is empty")
    return problems


def main():
    problems = validate(RANT)
    if problems:
        for problem in problems:
            print("ERROR: " + problem, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(RANT)
    # Round-trip check: the file the judge reads must be exactly the rant.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != RANT:
        print("ERROR: /output/entry.txt does not match the rant", file=sys.stderr)
        return 1
    print(RANT)
    print("Wrote %d characters to /output/entry.txt (verified)" % len(RANT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
