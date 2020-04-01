matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]

for t in zip(matrix_a, matrix_b):
    print(t)

r1 = [[sum(r) for r in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(r1)
