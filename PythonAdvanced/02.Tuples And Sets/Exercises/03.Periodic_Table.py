n = int(input())
table = set()

for _ in range(n):
    [table.add(chemical) for chemical in input().split()]

[print(chemical) for chemical in table]

"""
4
Ce O
Mo O Ce
Ee
Mo


3
Ge Ch O Ne
Nb Mo Tc
O Ne

"""