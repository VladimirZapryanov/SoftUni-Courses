rows, columns = [int(x) for x in input().split()]

matrix = []
match_squares = 0

for _ in range(rows):
    characters = input().split()
    matrix.append(characters)

for r in range(rows - 1):
    for c in range(columns - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            match_squares += 1

print(match_squares)