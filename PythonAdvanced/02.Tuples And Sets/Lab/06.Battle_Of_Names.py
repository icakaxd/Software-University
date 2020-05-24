n = int(input())
(even_set, odd_set) = set(), set()

for i in range(1, n+1):
    name = input()
    summed = sum([ord(x) for x in name]) // i
    if summed % 2 == 0:
        even_set.add(summed)
    else:
        odd_set.add(summed)


sum_even, sum_odd = sum(even_set), sum(odd_set)
# print(even_set)
if sum_even == sum_odd:
    print(', '.join([str(x) for x in odd_set.union(even_set)]))
elif sum_odd > sum_even:
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))

"""
4
Pesho
Stefan
Stamat
Gosho

6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan

"""