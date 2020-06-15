from collections import deque

parentheses = deque(p for p in input())
openings = []
is_valid = True

while parentheses:
    current = parentheses.popleft()
    if current in ['{', '[', '(']:
        openings.append(current)
    else:
        if openings:
            last = openings.pop()
            if (last == '{' and current != '}') or (last == '[' and current != ']') or (last == '(' and current != ')'):
                is_valid = False
        else:
            is_valid = False

if is_valid:
    print('YES')
else:
    print('NO')