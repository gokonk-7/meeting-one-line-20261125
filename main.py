"""The Meeting That Should Have Been One Line — make.fun bounty entry.

Writes one sentence to /output/entry.txt: the single line that could have
replaced an entire pointless meeting.

The line: the meeting outlived the project it served. The project is over,
but the recurring invite was never cancelled, so the meeting keeps showing
up to work — it is the only part of the project still employed. That is the
joke's turn: a meeting personified as the one employee who never got laid
off, which is why the line kills the meeting outright (its whole reason for
existing is gone), why it is relatable (everyone has a zombie recurring
meeting), and why it stands alone with no context needed.

Angle check against the visible field: the "decision already made",
"this could have been an email", "no update" and "the only action item is
another meeting" angles are all heavily used. The dead-project premise with
the still-employed punch is not — the closest entries are bare titles
("This Meeting Outlived Its Project") with no punchline attached.
"""

import os
import sys

# The sealed scorer's gate, per the kit's RULES.txt: 1 to 200 characters.
MAX_CHARS = 200

LINE = (
    "The project is over \u2014 this meeting is the only part of it "
    "still employed."
)


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what the grader will see.
    written = open(path, encoding="utf-8").read()
    if written != LINE or not 1 <= len(written) <= MAX_CHARS:
        print(f"verification failed for {path}", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
