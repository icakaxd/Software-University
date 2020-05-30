n = int(input())
matrix = []

for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()

for i in range(n):
    for k in range(n):
        if matrix[i][k] == symbol:
            print(f'({i}, {k})')


"""
3
ABC
DEF
X!@
!

"""