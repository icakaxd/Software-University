
expression = input()  # "1.txt.txt + (2.txt.txt - (2.txt.txt + 3) * 4 / (3 + 1.txt.txt)) * 5"

opening_brackets = []

for i in range(len(expression)):

    if expression[i] == "(":
        opening_brackets.append(i)
    elif expression[i] == ")":
        start_index = opening_brackets.pop()
        print(expression[start_index:i + 1])
