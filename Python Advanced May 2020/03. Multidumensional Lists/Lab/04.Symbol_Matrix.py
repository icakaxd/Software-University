n = int(input())
matrix = []

for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()
occurency = False
for i in range(n):
    if occurency:
        break
    for k in range(n):
        if matrix[i][k] == symbol:
            print(f'({i}, {k})')
            occurency = True

if not occurency:
    print(f'{symbol} does not occur in the matrix')


"""
3
ABC
DEF
X!@
!

"""