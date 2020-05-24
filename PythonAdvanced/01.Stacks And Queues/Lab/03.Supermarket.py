from collections import deque
queue = deque()
command = input()
while command != "End":
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()
else:
    print(f"{len(queue)} people remaining.")