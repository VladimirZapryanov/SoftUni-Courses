rows, columns = [int(x) for x in input().split()]
word = input()

matrix = []
word_index = 0

for r in range(rows):
    matrix.append([None] * columns)
    for c in range(columns):
        if r % 2 == 0:
            matrix[r][c] = word[word_index]
        else:
            matrix[r][columns - 1 - c] = word[word_index]
            
        word_index = (word_index + 1) % len(word)

for r in matrix:
    print("".join(r))
