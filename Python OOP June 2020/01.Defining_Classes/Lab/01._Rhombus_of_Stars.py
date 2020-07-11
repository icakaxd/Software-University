def generate_line(idx, n):
    indent = ' ' * (n - idx - 1)
    stars = '* ' * (idx + 1)
    return f'{indent}{stars}'[:-1:]


def print_rhombus(n):
    for i in range(n):
        print(generate_line(i, n))
    for i in range(n - 2, -1, -1):
        print(generate_line(i, n))


print_rhombus(1)
print_rhombus(2)
print_rhombus(3)
