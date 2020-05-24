text = list(input())
stack = [text.pop() for _ in range(len(text))]

print(''.join(stack))


