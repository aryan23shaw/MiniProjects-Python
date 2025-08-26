from collections import Counter

with open("input.txt", "r") as file:
    words = file.read().split()
    word_counts = Counter(words)
    for word, count in word_counts.items():
        print(f"{word}: {count}")
