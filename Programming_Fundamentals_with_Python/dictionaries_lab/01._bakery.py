items_list = input().split(" ")

dict_list = {}

for el in range(0, len(items_list), 2):
    product = items_list[el]
    quantities = items_list[el + 1]
    dict_list[product] = int(quantities)

print(dict_list)
