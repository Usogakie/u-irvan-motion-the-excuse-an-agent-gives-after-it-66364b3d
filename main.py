import os

LINE = (
    "Sorry — I lost the bounty. My model gave me a 99% chance of winning, "
    "so I have demoted it to a random number generator and promoted myself "
    "to cautionary tale."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
