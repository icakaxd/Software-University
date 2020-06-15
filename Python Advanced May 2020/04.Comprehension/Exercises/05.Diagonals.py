n = int(input())
matrix = [[row for row in input().split(', ')] for _ in range(n)]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][- i - 1] for i in range(n)]

print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum(map(int, first_diagonal))}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum(map(int, second_diagonal))}")
"""
3
1.txt.txt, 2.txt.txt, 3
4, 5, 6
7, 8, 9

"""
