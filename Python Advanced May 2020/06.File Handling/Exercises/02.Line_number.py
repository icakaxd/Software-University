#  icakad // Христо Дамянов
import string

i = 1
new_file = []
letters = string.ascii_lowercase + string.ascii_uppercase
punctuation = string.punctuation

with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        lette_len = sum([1 for x in line if x in letters])
        punct_len = sum([1 for x in line if x in punctuation])

        new_line = f"Line {i}: {line[0:len(line) - 1:]} ({lette_len})({punct_len})\n"
        new_file.append(new_line)
        i += 1

with open('output.txt', 'w') as file:
    file.writelines(new_file)
