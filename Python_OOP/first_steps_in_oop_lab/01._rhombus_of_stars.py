def print_line(spaces_count, stars_count):
    line_spaces = "".join([" "] * spaces)
    line_stars = " ".join(["*"] * stars)
    print(line_spaces + line_stars)


n = int(input())

for i in range(n):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)

for i in range(n - 2, -1, -1):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)
