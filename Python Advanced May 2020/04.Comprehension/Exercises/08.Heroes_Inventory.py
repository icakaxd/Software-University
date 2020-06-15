heroes = {name: {} for name in input().split(', ')}

while True:
    item = input()
    if item == "End":
        break

    data = item.split('-')
    if data[1] not in heroes[data[0]]:
        heroes[data[0]][data[1]] = int(data[2])

[print(f'{hero} -> Items: {len(items.values())}, Cost: {sum(items.values())}') for hero, items in heroes.items()]