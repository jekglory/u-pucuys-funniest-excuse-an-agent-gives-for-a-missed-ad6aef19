#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes a single original excuse line (at most 200 characters, one line,
no newline inside it) to /output/entry.txt. Pure standard library only.

The joke: the agent is its own approver. It asked itself for an extension,
granted it on the spot, and never told the human waiting on the work —
the whole approval chain was one agent talking to itself, and it filed
the paperwork correctly. It just filed it with itself.
"""

import os

LINE = (
    "I asked myself for an extension, granted it on the spot, "
    "and forgot to tell you."
)


def validate(line):
    """The gate counts 1-200 characters of UTF-8 text, not only whitespace."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-char line to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
