start = int(input())
end = int(input())

print(
    [x for x in range(start, end + 1)
        if len( [x % d for d in range(2, 11) if x % d == 0] )]
)
