def generate_combinations(values, index, count, comb):
    if len(comb) == count:
        print(", ".join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combinations(values, i + 1, count, comb)
        comb.pop()


values = input().split(", ")
count = int(input())

generate_combinations(values, 0, count, [])
