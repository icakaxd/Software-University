x, y = [int(x) for x in input().split()]
matrix = [[f"{chr(97 + j)}{chr(97 + j + i)}{chr(97 + j)}" for i in range(y)] for j in range(x)]
[print(' '.join(row)) for row in matrix]