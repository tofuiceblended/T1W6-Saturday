matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# print (matrix[0][1])

for rows in matrix:
    for item in rows:
        if item == rows[1]:
            print(item, end=" ")
    print()


# 3by3 matrix
