x, y = [int(x) for x in input().split()]
matrix = [[f"{chr(j)}{chr(j + i)}{chr(j)}" for i in range(y)] for j in range(97, 97 + x)]
[print(' '.join(row)) for row in matrix]