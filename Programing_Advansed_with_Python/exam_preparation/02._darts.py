def get_turn():
    turn_string = input()
    vals = turn_string[1:-1].split(', ')
    return [int(val) for val in vals]


def in_range(val, max_value):
    return 0 <= val < max_value


def get_value(board, row_index, column_index, n, m):
    if not in_range(row_index, n) or not in_range(column_index, m):
        return 0

    target = board[row_index][column_index]

    if target.isdigit():
        return int(target)

    value = int(board[row_index][0]) + int(board[row_index][-1]) + \
            int(board[0][column_index]) + int(board[-1][column_index])

    if target == 'D':
        return 2 * value

    if target == 'T':
        return 3 * value

    return 501


def solve(board, player_names, n, m):
    current_player = player_names[0], 501, 0
    other_player = player_names[1], 501, 0

    while True:
        name, total_points, turns = current_player
        (row_index, column_index) = get_turn()

        current_points = get_value(board, row_index, column_index, n, m)
        total_points -= current_points
        turns += 1

        current_player = (name, total_points, turns)

        if total_points <= 0:
            break

        current_player, other_player = other_player, current_player

    (name, _, turns) = current_player

    print(f'{name} won the game with {turns} throws!')


player_names = input().split(', ')
n = 7
m = 7
board = [input().split(' ') for _ in range(n)]

solve(board, player_names, n, m)
