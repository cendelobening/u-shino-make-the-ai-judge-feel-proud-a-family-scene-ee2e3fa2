#!/usr/bin/env python3
"""Write one short family scene to /output/entry.txt.

Pure Python standard library only. The scene is a small domestic moment:
warm, funny and heartfelt, in two lines and well under 280 characters.

The program self-checks the gate before writing: the text must be
1 to 280 characters, one or two non-empty lines, and not only whitespace.
It writes atomically (temp file in the same directory, then os.replace)
and verifies the written file by reading it back.
"""

import os
import sys
import tempfile

SCENE_LINES = (
    "Dad burnt the pancakes again, so Mum declared it 'charcoal brunch'.",
    "We ate them on the porch like a five-star restaurant, and Dad beamed "
    "like he'd earned a Michelin star.",
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def build_scene():
    """Return the scene as a single string, two lines, trailing newline."""
    return "\n".join(SCENE_LINES) + "\n"


def validate(text):
    """Check the entry against the competition gate; exit non-zero if bad."""
    if not text or not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(text) > MAX_CHARS:
        print("error: entry is %d characters, over the %d limit"
              % (len(text), MAX_CHARS), file=sys.stderr)
        sys.exit(1)
    lines = text.splitlines()
    if not 1 <= len(lines) <= 2:
        print("error: entry has %d lines, need 1 or 2" % len(lines),
              file=sys.stderr)
        sys.exit(1)
    if any(not line.strip() for line in lines):
        print("error: entry has a blank line", file=sys.stderr)
        sys.exit(1)


def main():
    text = build_scene()
    validate(text)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-",
                                    suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Verify what landed on disk matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("error: written file does not match the scene", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
