targets = [int(el) for el in input().split()]
index = input()

counter_shot_targets = 0

while not index == "End":
    index = int(index)

    if index not in range(len(targets)):
        index = input()
        continue

    current_value = targets[index]

    if current_value == -1:
        index = input()
        continue

    targets[index] = -1
    counter_shot_targets += 1

    for current_index in range(len(targets)):
        if targets[current_index] == -1:
            continue
        if targets[current_index] > current_value:
            targets[current_index] -= current_value
        else:
            targets[current_index] += current_value

    index = input()

print(f"Shot targets: {counter_shot_targets} -> {' '.join([str(el) for el in targets])}")