numbers_str_list = input().split()
n = int(input())

numbers_list = [int(x) for x in numbers_str_list]

print(" -> ".join([str(x) for x in numbers_list]))
