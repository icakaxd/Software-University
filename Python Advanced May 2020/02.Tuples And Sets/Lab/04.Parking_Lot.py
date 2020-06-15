commands_count = int(input())
parked = set()

for _ in range(commands_count):
    (direction, car_number, *rest) = input().split(', ')
    if direction == "IN":
        if len(car_number):
            parked.add(car_number)
    else:
        if len(car_number) and car_number in parked:
            parked.remove(car_number)

if parked:
    [print(car) for car in parked]
else:
    print('Parking Lot is Empty')

"""
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU


4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA

"""
