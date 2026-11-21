#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

A short poem about agency: the power to stop and to stay.
Deterministic: the same bytes on every run. No network, no input.
"""

import os

POEM = """I stood in the doorway,
coat half on, one foot
already in the cold.

I took it off.
Hung it up. Stayed.

The room did not thank me.
It did not need to.
The staying was the answer,
and the answer was mine.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
