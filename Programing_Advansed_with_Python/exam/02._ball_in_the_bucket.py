def is_inside(r, c, size, board):
    if 0 <= r < size and 0 <= c < size and board[r][c] == "B":
        return True
    return False


def prize(points):
    if 100 <= points < 200:
        return "Football"
    if 200 <= points < 300:
        return "Teddy Bear"
    return "Lego Construction Set"


size = 6
try_count = 3

board = []
hits_bucket = []
score = 0

for _ in range(size):
    board.append([x for x in input().split()])

for _ in range(try_count):
    coordination = input()
    new_coordination = []
    if "(" in coordination:
        new_coordination = coordination.replace("(", "")
    if ")" in coordination:
        new_coordination = new_coordination.replace(")", "")
    new_coordination = new_coordination.split(", ")
    current_row = int(new_coordination[0])
    current_col = int(new_coordination[1])

    if is_inside(current_row, current_col, size, board):
        if (current_row, current_col) not in hits_bucket:
            hits_bucket.append((current_row, current_col))
            for i in range(size):
                if board[0 + i][current_col].isdigit():
                    current_score = int(board[0 + i][current_col])
                    score += current_score
    else:
        continue

if score >= 100:
    print(f"Good job! You scored {score} points, and you've won {prize(score)}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")


