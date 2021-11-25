people = int(input())
wagons = [int(el) for el in input().split()]

while people > 0 and sum(wagons) < len(wagons) * 4:
    people -= 1
    for i in range(len(wagons)):
        if wagons[i] < 4:
            wagons[i] += 1
            break

if sum(wagons) < len(wagons) * 4:
    print("The lift has empty spots!")
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
print(*wagons)