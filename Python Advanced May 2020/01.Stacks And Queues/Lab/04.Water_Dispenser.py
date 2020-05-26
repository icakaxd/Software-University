from collections import deque

liters_in_dispenser = int(input())
people = deque()

name = input()
while name != "Start":
    people.append(name)
    name = input()


command = input().split()
while command[0] != "End":

    if len(command) == 2:
        liters_in_dispenser += int(command[1])
    else:
        person = people.popleft()
        liters = int(command[0])
        print(liters)
        if liters_in_dispenser >= liters:
            liters_in_dispenser -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")


else:
   print(f"{liters_in_dispenser} liters left")