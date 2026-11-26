"""make.fun entry: Five Seconds to Explain the Glass.

Writes the house cat's official one-sentence excuse to /output/entry.txt.
"""

ENTRY = (
    "That glass was squatting in my sunbeam for three hours, so I evicted it, "
    "and the shattering was its own fault; I would do it again."
)


def main():
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)


if __name__ == "__main__":
    main()
