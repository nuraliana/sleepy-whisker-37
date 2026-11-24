"""Write the chosen one-star cat review to entry.txt.

Stdlib only. The entry is a fixed string; this program copies it
exactly (no trailing newline) into entry.txt inside the folder named
by MAKEFUN_OUTPUT_DIR, or /output when that variable is unset.
"""

import os

ENTRY = "One star. He let me see the bottom of my food bowl. The bottom. I am not an animal."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
