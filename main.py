#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
No network, no input: the text is fixed in this file.

The story: she kept another man's letters, and burned the narrator's.
Two acts, one turn — a love triangle told in a single breath.
"""

import os

STORY = "She kept his letters. Burned mine."

def main():
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"story must be 1-60 chars, got {len(STORY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
