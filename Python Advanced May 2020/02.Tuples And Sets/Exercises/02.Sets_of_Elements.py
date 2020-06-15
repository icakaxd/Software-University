n_len, m_len = [int(x) for x in input().split()]

n = {input() for _ in range(n_len)}
m = {input() for _ in range(m_len)}

[print(x) for x in n & m]

"""
4 3
1.txt.txt
3
5
7
3
4
5

"""
