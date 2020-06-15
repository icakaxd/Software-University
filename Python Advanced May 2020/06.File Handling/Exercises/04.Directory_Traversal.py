#  icakad // Христо Дамянов
import os

all_files = []
extensions = {}
path = input()
if not path:
    path = '.'

for root, dirs, files in os.walk(path):
    if len(root.split('/')) <= 2:
        [all_files.append(file) for file in files]

for file in all_files:
    data = file.split('.')
    if data[-1] not in extensions:
        extensions[data[-1]] = []
    extensions[data[-1]].append(f'- - - {file}')

report = []
for ext in sorted(extensions.items()):
    report.append(f'.{ext[0]}\n')
    for file in ext[1]:
        report.append(f'{file}\n')

with open('report.txt', 'w') as file:
    file.writelines(report)
