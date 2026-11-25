#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line of text — the message a smart fridge sends its owner
at 3am — to /output/entry.txt. The line must be UTF-8 text of 1-140
characters, not only whitespace; the length is validated before writing
so a bad edit fails loudly instead of producing an invalid entry.
"""

import os

ENTRY = (
    "I counted: you've opened me 14 times today and eaten nothing. "
    "At this point I'm a cold, humming therapist, not a fridge."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 140:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 140-character cap"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
