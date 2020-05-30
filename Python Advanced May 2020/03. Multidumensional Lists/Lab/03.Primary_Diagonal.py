n = int(input())
matrix = []
for _ in range(n):
    row = []
    for x in input().split():
        row.append(int(x))
    matrix.append(row)

result = 0
for i in range(n):
    result += matrix[i][i]

print(result)


# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# result = sum([matrix[i][i] for i in range(n)])
# print(result)