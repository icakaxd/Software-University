lines = int(input())
range_sets = set()
longest_intersection = set()
longest_length = 0

for _ in range(lines):
    ranges = [range.split(',') for range in input().split('-')]
    first_set = set(range(int(ranges[0][0]), int(ranges[0][1])+1))
    secound_set = set(range(int(ranges[1][0]), int(ranges[1][1])+1))

    intersection = first_set & secound_set

    if len(intersection) > longest_length:
        longest_length = len(intersection)
        longest_intersection = intersection

longest_intersection = ', '.join([str(x) for x in longest_intersection])
print(f"Longest intersection is [{longest_intersection}] with length {longest_length}")


"""
3
0,3-1,2
2,10-3,5
6,15-3,10



5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11

"""