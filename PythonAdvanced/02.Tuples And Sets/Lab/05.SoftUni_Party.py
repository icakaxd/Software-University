n = int(input())
invates = sorted(reversed([input() for _ in range(n)]))
guest_list = set()
vip_list = set()

guest = input()
while guest != "END":
    if guest in invates:
        invates.remove(guest)
        vip_list.add(guest) if guest[0].isdigit() else guest_list.add(guest)
    guest = input()

print(len(invates))
[print(invate) for invate in invates if invate[0].isdigit()]
[print(invate) for invate in invates if not invate[0].isdigit()]

"""
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END

"""