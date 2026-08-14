
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
transposed_matrix = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(list[i])
    transposed_matrix.append(transposed_row)
#alternative transposed_matrix = [list(row) for row in zip(*matrix)]

print("Original matrix:", matrix)
print("Transposed matrix:", transposed_matrix)

