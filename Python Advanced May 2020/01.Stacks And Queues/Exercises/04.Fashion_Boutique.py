def solve():
    clothes_in_box = [int(c) for c in input().split()]
    rack_capacity = int(input())
    current_rack = 0
    racks = 1

    while clothes_in_box:
        current_piece = clothes_in_box.pop()
        if (current_rack + current_piece) > rack_capacity:
            racks += 1
            current_rack = current_piece
        else:
            current_rack += current_piece

    print(racks)


solve()
