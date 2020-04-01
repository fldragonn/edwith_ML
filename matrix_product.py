matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]

print("matrix_a is")
for r in matrix_a:
    print(r)

print("*matrix_b is")
print(*matrix_b)

print("zip(*matrix_b) is")
for c in zip(*matrix_b):
    print(c)

result = [ [sum(a * b for a, b in zip(row_a, column_b))
            for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)