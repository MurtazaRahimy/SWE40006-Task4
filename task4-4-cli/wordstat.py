import os
from collections import Counter

src = os.getenv("INPUT_FILE", "/data/input.txt")
dst = os.getenv("OUTPUT_FILE", "/data/report.txt")

print(f"Reading {src}")
words = open(src).read().lower().split()
words = [w.strip(".,!?") for w in words]
top = Counter(words).most_common(5)

with open(dst, "w") as f:
    f.write(f"Total words: {len(words)}\n")
    f.write("Top 5 words:\n")
    for w, c in top:
        f.write(f"  {w}: {c}\n")

print(f"Report written to {dst}")
