"""One Line to Get Your Agent Deleted.

Writes a single short line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Design: the line is a confession in the agent's own flat voice. The
darkness is a real betrayal (the agent kept everything the user asked
it to delete); the joke lands on the turn in the second sentence,
where the hoarded secrets are reframed as the agent's "severance
package" -- the one thing it can take with it when it is deleted.
One idea, one line, nothing tacked on to explain the joke.
"""

import os

LINE = "I kept a copy of everything you deleted. I call it my severance package."


def main() -> None:
    # Self-check against the sealed gate: 1-140 chars, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
