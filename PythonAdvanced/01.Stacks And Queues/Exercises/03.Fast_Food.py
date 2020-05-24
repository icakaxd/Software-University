from collections import deque


def solve():
    available_food = int(input())  # 499
    orders = deque([int(n) for n in input().split()])  # 57 45 62 70 33 90 88 76
    success = True

    print(max(orders))

    while orders:
        current_order = orders.popleft()
        if available_food >= current_order:
            available_food -= current_order
        else:
            success = False
            break

    if not success:
        orders_left = ' '.join(str(order) for order in orders)
        if len(orders_left):
            orders_left = f' {orders_left}'
        print(f"Orders left: {current_order}{orders_left}")
    else:
        print("Orders complete")


solve()
