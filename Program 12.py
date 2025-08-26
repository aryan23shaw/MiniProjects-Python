from collections import Counter

with open("input.txt", "r") as file:
    words = file.read().split()
    word_counts = Counter(words)
    duplicates = [word for word, count in word_counts.items() if count > 1]
    print("Duplicate words:", duplicates)
