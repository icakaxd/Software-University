contacts = {}

command = input()
while not command.isdigit():
    name, number = command.split('-')
    contacts[name] = number
    command = input()
else:
    for _ in range(int(command)):
        name = input()
        if name not in contacts:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {contacts[name]}")

"""
Adam-0888080808
2
Mery
Adam


Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf

"""