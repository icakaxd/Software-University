from random import randint

BOARD_SIZE = 3


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __repr__(self):
        return f'Name: {self.name}, Mark: {self.mark}'


def print_board(board):
    for row in board:
        values = []
        for cell in row:
            if cell is None:
                values.append(' ')
            else:
                values.append(cell)
        values_str = ' | '.join(values)
        print(f'| {values_str} |')


def setup_board(size):
    return [[None] * size for _ in range(size)]


def setup_player(mark='X'):
    # name = input('Name: ')
    # if not mark:
    #     mark = input('Mark: ').upper()
    # else:
    #     print(f'Mark: {mark}')
    # return Player(name, mark)
    return Player(f'Player_{randint(1, 10)}', mark)


def setup():
    player_one = setup_player()
    player_two = setup_player('O' if player_one.mark == 'X' else 'O')
    board = setup_board(BOARD_SIZE)
    return (board, player_one, player_two)


def game_loop():
    pass


def start_game():
    (board, *players) = setup()
    print_board(board)
    print(players)


start_game()
