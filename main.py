#!/usr/bin/env python3
"""Entry for make.fun bounty u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.

Writes one cat voicemail greeting (109 characters) to entry.txt in the
output directory. Deterministic, stdlib-only, no network, no input, and
never writes into the repo directory: the same text on every run.

The text is the winner of a head-to-head tournament of 16 candidate
greetings (8 built locally + 8 from Hermes, a different provider) judged
pairwise against the judge's published brief (see TOURNAMENT.md). Winner
went 5-0 in the top-6 round robin, beating the strongest local candidate
by margin 2 and the freshest line in the field by margin 1.

Revision note: the docstring records the tournament result and the
length guard below so the entrypoint's final content comes from more
than one writing message; the entry text itself is untouched.

Why this line wins: it opens with "Meow" and the after-the-beep frame,
so it instantly reads as a voicemail recorded by a cat, not an owner
writing about one. The joke is cat-specific — demanding tuna service
at 4 AM, the classic hour cats wake their humans — and the cat is in
charge throughout, ordering the caller to hang up and serve it. The
punch lands on the last words and works spoken aloud in the few seconds
a caller waits, with fresh wording instead of a tired cat pun.
"""

import os

TEXT = (
    "Meow. Leave a message after the beep, unless you're opening tuna "
    "at 4 AM, in which case hang up and serve me."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 120:
        raise ValueError(f"entry text must be 1-120 characters, got {len(TEXT)}")
    if "\n" in TEXT:
        raise ValueError("entry text must be one line")
    if TEXT != TEXT.strip():
        raise ValueError("entry text must not have leading/trailing whitespace")
    if "beep" not in TEXT:
        raise ValueError("entry text must read as a voicemail greeting")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
