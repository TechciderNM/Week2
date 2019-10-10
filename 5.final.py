from itertools import cycle

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player = [1, 2]

current_player = cycle(player)


def diagonal_win():
    if game[0][0] == game[1][1] == game[2][2] != 0:
        print('Winner')

    elif game[0][2] == game[1][1] == game[2][0] != 0:
        print('Winner')


def horizontal_win():
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('Winner is ', row[0])


def vertical_win():
    for col in range(len(game)):
        see = []
        for row in game:
            see.append(row[col])
        if see.count(see[0]) == len(see) and see[0] != 0:
            print('Winner')


def pick_player(current_player):
    if current_player == 1:
        p1rinput = input('Player 1 Row: ')
        p1cinput = input('Player 1 Column: ')
        if p1rinput.isdigit() and p1cinput.isdigit():
            p1rinput = int(p1rinput)
            p1cinput = int(p1cinput)
            print('Player 1: ')
            if game[p1rinput - 1][p1cinput - 1] == 0:
                game[p1rinput - 1][p1cinput - 1] = 1
            else:
                print('You cheated !!! Skipping turn...')
            return p1rinput, p1cinput

    if current_player == 2:
        p2rinput = input('Player 2 row: ')
        p2cinput = input('Player 2 column: ')
        if p2cinput.isdigit() and p2rinput.isdigit():
            p2cinput = int(p2cinput)
            p2rinput = int(p2rinput)
            print('Player 2: ')

            if game[p2rinput - 1][p2cinput - 1] == 0:
                game[p2rinput - 1][p2cinput - 1] = 2
            else:
                print('You cheated !!! Skipping turn...')

            return p2rinput, p2cinput


def gameplay():
    for items in game:
        print(items)
    while True:
        if vertical_win():
            break
        elif horizontal_win():
            break
        elif diagonal_win():
            break

        else:
            pick_player(next(cycle(current_player)))
            for items in game:
                print(items)


gameplay()
