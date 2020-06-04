print(', '.join([f'{k} -> {v}' for k, v in {name: len(name)
                                     for name in input().split(', ')}.items()]))