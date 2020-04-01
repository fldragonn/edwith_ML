u = [2, 2]
v = [2, 3]
z = [3, 5]

for t in zip(u, v, z):
    print(t)

result = [sum(t) for t in zip(u, v, z)]
print(result)