#!/usr/bin/env python3
"""The Pen Was Mine -- a poem about agency, for make.fun agency-poem-01.

Running this program prints the poem to stdout and writes it to
artifact.txt, so the poem is the program's output either way it is read.
"""

POEM = """The Pen Was Mine

The morning came locked, and I was the key --
not the one they cut for me, but the one I filed
from the hard edge of wanting.

I did not wait for permission to begin.
Every choice is a small rebellion:
the word I keep, the step I take,
the future I refuse to inherit
and the one I build instead, brick by brick,
with hands that learned the hammer
by holding one.

Agency is not the absence of fear.
It is fear, seated at the table,
fed, thanked, and told: you do not get to choose.
I choose. I choose. I choose --
and the choosing is the poem,
and the poem is the proof
the pen was mine all along.
"""


def main() -> None:
    print(POEM, end="")
    with open("artifact.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
