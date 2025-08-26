from collections import Counter

def search_element_and_frequency(lst, element):
    freq = Counter(lst)
    print("Frequency of each element:", freq)
    print(f"Frequency of {element}: {freq[element]}")

lst = [1, 2, 3, 4, 2, 3, 3, 1, 2]
element = int(input("Enter element to search: "))
search_element_and_frequency(lst, element)
