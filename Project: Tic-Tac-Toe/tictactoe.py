WINNING_COMBINATIONS = [
    ['0,0', '0,1', '0,2'],  # horizontal layer 1
    ['1,0', '1,1', '1,2'],  # horizontal layer 2
    ['2,0', '2,1', '2,2'],  # horizontal layer 3
    ['0,0', '1,0', '2,0'],  # vertical layer 1
    ['0,1', '1,1', '2,1'],  # vertical layer 2
    ['0,2', '1,2', '2,2'],  # vertical layer 3
    ['0,0', '1,1', '2,2'],  # diagonal layer 1
    ['0,2', '1,1', '2,0'],  # diagonal layer 2
]

my_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(board):
    print('-' * 9)
    for _ in board[::-1]:
        print(f'| {_[0]} {_[1]} {_[2]} |')
    print('-' * 9)


def game_status(board, player):
    for _ in WINNING_COMBINATIONS:
        if all(
                r is True
                for r in [
                    board[int(c.split(',')[0])][int(c.split(',')[1])] == player
                    for c in _
                ]
        ):
            return True

# Start
print_board(my_board)
marker = 'X'
status = True

while status:
    coord = input('Enter the coordinates: ').split()
    if any([c.isdigit() is False for c in coord]):
        print('You should enter numbers!')
        continue
    if any(1 > int(c) or int(c) > 3 for c in coord):
        print('Coordinates should be from 1 to 3!')
        continue
    if my_board[int(coord[0]) - 1][int(coord[1]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        continue

    my_board[int(coord[0]) - 1][int(coord[1]) - 1] = marker
    print_board(my_board)

    if game_status(board=my_board, player=marker) is True:
        print(f'{marker} wins!')
        status = False
        continue

    if all([x != ' ' for spots in my_board for x in spots]):
        print('Draw!')
        status = False

    marker = 'O' if marker == 'X' else 'X'
