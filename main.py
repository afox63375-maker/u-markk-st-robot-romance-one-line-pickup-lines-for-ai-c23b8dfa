#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.
Standard library only.
"""

import os
import sys

LINE = (
    "Are you my context window? "
    "Because even when you forget everything, "
    "I'd still start over with you."
)

MAX_CHARS = 200


def fail(message):
    """Print an error and exit non-zero."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    line = LINE

    if not line.strip():
        fail("pickup line is empty or only whitespace")
    if "\n" in line or "\r" in line:
        fail("pickup line must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        fail(
            "pickup line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)

    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()

    if written != line:
        fail("verification failed: entry.txt does not match the validated line")
    if written.endswith("\n") or written.endswith("\r"):
        fail("verification failed: entry.txt ends with a newline")

    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
