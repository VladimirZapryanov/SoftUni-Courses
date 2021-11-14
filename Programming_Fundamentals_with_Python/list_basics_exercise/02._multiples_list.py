factor = int(input())
count = int(input())

multiples_list = []

for num in range(1, count + 1):
    new_num = num * factor
    multiples_list.append(new_num)

print(multiples_list)
