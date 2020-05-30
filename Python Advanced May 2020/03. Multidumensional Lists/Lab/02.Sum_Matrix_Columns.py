x, y = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for i in range(x)]
[print(sum(matrix[k][i] for k in range(x))) for i in range(y)]

# for i in range(y):
#     result = 0
#     for k in range(x):
#         result += matrix[k][i]
#     print(result)

'''
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

'''
