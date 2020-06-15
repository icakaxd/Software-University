#  icakad // Христо Дамянов
import os

while True:
    command = input()

    if command == 'End':
        break

    cmd = command.split('-')
    file = cmd[1]

    if cmd[0] == 'Create':
        with open(file, 'w') as file:
            file.write('')

    if cmd[0] == 'Add':
        content = cmd[2] + "\n"
        try:
            with open(file, 'a') as file:
                file.write(content)
        except Exception as e:
            print(e)

    if cmd[0] == 'Replace':
        lines = []
        new_lines = []
        try:
            with open(file, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            print(e)

        for line in lines:
            new_line = line.replace(cmd[2], cmd[3])
            new_lines.append(new_line)
        try:
            with open(cmd[1], 'w') as file:
                file.writelines(new_lines)
        except Exception as e:
            print(e)

    if cmd[0] == 'Delete':
        try:
            os.unlink(file)
        except Exception as e:
            print(e)
