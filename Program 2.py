def search_frequency(lst, element):
    count = lst.count(element)
    print(f"Frequency of {element}: {count}")

lst = [1, 2, 3, 4, 2, 3, 3, 1, 2]
element = int(input("Enter element to search: "))
search_frequency(lst, element)
