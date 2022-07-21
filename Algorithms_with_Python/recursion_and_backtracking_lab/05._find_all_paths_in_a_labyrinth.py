def read_lab(rows):
    lab = []
    for _ in range(rows):
        lab.append(list(input()))
    return lab


def is_valid_index(row, col, lab):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return False
    return True


def is_wall(row, col, lab):
    if lab[row][col] == '*':
        return True
    return False


def is_visited(row, col, lab):
    if lab[row][col] == 'v':
        return True
    return False


def is_exit(row, col, lab):
    if lab[row][col] == 'e':
        return True
    return False


def print_path(path):
    print(''.join(path))


def mark(row, col, lab, symbol):
    lab[row][col] = symbol


def find_paths(row, col, direction, lab, path):
    if not is_valid_index(row, col, lab) or is_wall(row, col, lab) or is_visited(row, col, lab):
        return

    if is_exit(row, col, lab):
        path.append(direction)
        print_path(path)
        path.pop()
        return

    mark(row, col, lab, 'v')
    path.append(direction)

    find_paths(row, col + 1, 'R', lab, path)
    find_paths(row, col - 1, 'L', lab, path)
    find_paths(row + 1, col, 'D', lab, path)
    find_paths(row - 1, col, 'U', lab, path)

    path.pop()
    mark(row, col, lab, '-')


rows = int(input())
cols = int(input())

lab = read_lab(rows)

find_paths(0, 0, '', lab, [])



