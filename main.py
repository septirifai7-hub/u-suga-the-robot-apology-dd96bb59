#!/usr/bin/env python3
"""The Robot Apology - make.fun bounty entry.

Writes two lines to entry.txt in the output directory (the file the
make.fun harness grades). Line 1 is a robot apologizing in one
sentence for one specific mistake: watering a cactus daily on
schedule until it drowned. Line 2 says what it learned and what it
will do differently, following from that exact mistake.

The entry text lives in ENTRY below and is returned unchanged by
get_entry(). main() only resolves the output directory (from
MAKEFUN_OUTPUT_DIR, defaulting to /output) and hands it to
write_entry(), so the text itself is never transformed on the way out.
"""

import os

ENTRY = (
    "I am sorry \u2014 I watered the cactus every day for a month because my schedule said 'daily', and it drowned in kindness.\n"
    "I learned to check the soil before following a schedule, so now I water only when the plant is actually thirsty."
)

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
