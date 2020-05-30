x, y = input().split(', ')
matrix = []

for _ in range(int(x)):
    row = []
    for x in input().split(', '):
        row.append(int(x))
    matrix.append(row)

sums = 0
for row in matrix:
    sums += sum(row)

print(sums)
print(matrix)

# x, y = input().split(', ')
# matrix = [[int(x) for x in input().split(', ')] for _ in range(int(x))]
# sums = sum([sum(row) for row in matrix])
# print(sums)
# print(matrix)
