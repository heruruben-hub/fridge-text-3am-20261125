import os

ENTRY_TEXT = "I counted: you've opened me 14 times today and eaten nothing. At this point I'm a cold, humming therapist, not a fridge."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY_TEXT.strip()
    if len(text) < 1 or len(text) > 140:
        raise ValueError(
            f"Entry text must be 1-140 characters long, got {len(text)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
