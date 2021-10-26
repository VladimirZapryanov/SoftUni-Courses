first = input()
second = input()

for num_1 in range(int(first[0]), int(second[0]) + 1):
    for num_2 in range(int(first[1]), int(second[1]) + 1):
        for num_3 in range(int(first[2]), int(second[2]) + 1):
            for num_4 in range(int(first[3]), int(second[3]) + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    barcode = str(num_1)+str(num_2)+str(num_3)+str(num_4)
                    print(barcode, end=" ")






