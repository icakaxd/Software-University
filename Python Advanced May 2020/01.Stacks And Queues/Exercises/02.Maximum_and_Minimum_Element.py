def solve():
    number_of_queries = int(input())
    elements = []

    for _ in range(number_of_queries):

        command = [int(n) for n in input().split()]
        query = command[0]
        if len(command) > 1:
            element = command[1]

        if query == 1:
            elements.append(element)
        elif query == 2 and len(elements):
            elements.pop()
        elif query == 3:
            if len(elements):
                print(max(elements))
        elif query == 4:
            if len(elements):
                print(min(elements))

    print(', '.join([str(el) for el in reversed(elements)]))


solve()
