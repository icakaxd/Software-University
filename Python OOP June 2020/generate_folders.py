import os

idx = 1
while True:
    dir_name = input()
    if dir_name:
        if dir_name == 'End':
            break
        dir_name = f'{idx:02d}.{dir_name.title().replace(" ", "_")}'

        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            os.mkdir(f'{dir_name}/Lab')
            os.mkdir(f'{dir_name}/Exercises')
        idx += 1
