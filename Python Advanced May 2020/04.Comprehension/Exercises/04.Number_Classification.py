numbers = input().split(', ')

[print(f'{k}: {v}') for k, v in {'Positive': ', '.join(x for x in numbers if int(x) >= 0),
           'Negative': ', '.join(x for x in numbers if int(x) < 0),
           'Even': ', '.join(x for x in numbers if int(x) % 2 == 0),
           'Odd': ', '.join(x for x in numbers if int(x) % 2 != 0)}.items()]

"""
1.txt.txt, -2.txt.txt, 0, 5, 3, 4, -100, -20, 12, 19, -33

"""
