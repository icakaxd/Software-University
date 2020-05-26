def solve():
    numbers = [n for n in input().split()]
    reversed_numbers = []

    for _ in range(len(numbers)):
        reversed_numbers.append(numbers.pop())

    result = ' '.join(reversed_numbers)
    print(result)

solve()