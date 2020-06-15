line = input()
present = {}

for ch in line:
    if ch not in present:
        present[ch] = 0
    present[ch] += 1

[print(f"{ch}: {count} time/s") for (ch, count) in sorted(present.items())]

"""
SoftUni rocks
"""