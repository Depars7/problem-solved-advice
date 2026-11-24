"""Write the one-line worst AI advice entry to /output/entry.txt.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 140
characters, not only white space, and exactly one line, written with
no trailing newline. The line is assembled from three parts so each
clause can be tightened on its own: the setup (delete the failing
test), the bogus logic (no report, no error), and the smug sign-off.
"""

import os

PARTS = (
    "Your code has a bug? Delete the failing test — ",
    "if nothing reports the error, the error no longer exists. ",
    "Problem solved!",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 140, "entry must be 1 to 140 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
