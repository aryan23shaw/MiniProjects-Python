def count_odd_even(t):
    odd = len([x for x in t if x % 2 != 0])
    even = len(t) - odd
    print(f"Odd numbers: {odd}, Even numbers: {even}")

t = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
count_odd_even(t)
