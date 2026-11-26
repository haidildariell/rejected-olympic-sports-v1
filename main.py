#!/usr/bin/env python3
"""Rejected Olympic Sports entry.

Writes exactly one line of text to /output/entry.txt.
No arguments, no network.
"""

import os

ENTRY = "Synchronized Eye-Rolling: four judges score your teenager's sigh; Russia leads after a flawless 'whatever' in the final rotation."

DEFAULT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check an entry line is 1-200 chars and not whitespace-only.

    Raises ValueError on failure.
    """
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry line must not be whitespace-only")
    return line


def write_entry(line, path=DEFAULT_PATH):
    """Create the output directory and write one line as UTF-8."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    """Validate the entry line, then write it to the output file."""
    validate_line(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
