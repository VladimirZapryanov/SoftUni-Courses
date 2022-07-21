def find_paths(row, col, direction, lab, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    if lab[row][col] == 'e':
        path.append(direction)
        print(''.join(path))
        path.pop()
        return

    lab[row][col] = 'v'
    path.append(direction)

    find_paths(row, col + 1, 'R', lab, path)
    find_paths(row, col - 1, 'L', lab, path)
    find_paths(row + 1, col, 'D', lab, path)
    find_paths(row - 1, col, 'U', lab, path)

    path.pop()
    lab[row][col] = '-'


def read_lab(rows):
    lab = []
    for _ in range(rows):
        lab.append(list(input()))
    return lab


rows = int(input())
cols = int(input())

lab = read_lab(rows)

find_paths(0, 0, '', lab, [])



