n = int(input())
invites = sorted(reversed([input() for _ in range(n)]))
guest_list = set()
vip_list = set()

guest = input()
while guest != "END":
    if guest in invites:
        invites.remove(guest)
        vip_list.add(guest) if guest[0].isdigit() else guest_list.add(guest)
    guest = input()

print(len(invites))
[print(invite) for invite in invites if invite[0].isdigit()]
[print(invate) for invate in invites if not invate[0].isdigit()]
