row = [[x for x in item.split(' ') if len(x) > 0] for item in input().split('|')]
print(' '.join([' '.join(rr) for rr in reversed(row)]))


"""
1 2 3 |4 5 6 | 7 8

"""