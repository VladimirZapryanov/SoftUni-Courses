lines = int(input())
total_sum = 0

for line in range(lines):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")