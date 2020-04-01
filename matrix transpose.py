matrix_a = [[1,2,3], [4,5,6]]
for t in matrix_a:
    print(t)

print()
print("*matrix_a is")
print(*matrix_a)

for t in zip(*matrix_a):
    print(t)

result = [ [element for element in t] for t in zip(*matrix_a)]
print(result)