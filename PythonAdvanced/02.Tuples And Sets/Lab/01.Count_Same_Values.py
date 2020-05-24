numbers = tuple(map(float, input().split()))

occurances = {}
for num in numbers:
    if not num in occurances:
        occurances[num] = 0
    occurances[num] += 1

[print(f"{key} - {value} times") for key, value in occurances.items()]
