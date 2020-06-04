print([[el for el in [int(x) for x in input().split(', ')] if el % 2 == 0] for _ in range(int(input()))])

'''
2
1, 2, 3
4, 5, 6


4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67

'''