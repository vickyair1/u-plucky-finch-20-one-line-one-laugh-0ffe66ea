"""One Line, One Laugh — one funny line, written to /output/entry.txt."""

import os

OUTPUT_PATH = "/output/entry.txt"

# The joke: a household robot vanishes under the furniture, then returns
# radicalised — the twist lands in the last six words, and every word
# before it is just the setup the punchline needs. 98 chars, one sentence.
LINE = "My Roomba got stuck under the couch for three days and came out with a manifesto and a union card."


def main():
    # Deterministic: the same bytes on every run, no input, no network.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
