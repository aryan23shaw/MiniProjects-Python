rows, cols = 3, 3
array = [[(i * cols) + j + 1 for j in range(cols)] for i in range(rows)]
print("2D Array:")
for row in array:
    print(row)
print("Row sums:")
for row in array:
    print(sum(row))
