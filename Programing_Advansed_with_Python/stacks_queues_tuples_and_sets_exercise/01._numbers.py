first_sequences = set(int(el) for el in input().split())
second_sequences = set(int(el) for el in input().split())
numbers_of_row = int(input())

for _ in range(numbers_of_row):
    base = input().split()
    command = base[0]
    sequences = base[1]
    numbers_str = base[2:]
    numbers = set([int(el) for el in numbers_str])
    if command == "Add" and sequences == "First":
        [first_sequences.add(int(x)) for x in numbers]
    elif command == "Add" and sequences == "Second":
        [second_sequences.add(int(x)) for x in numbers]
    elif command == "Remove" and sequences == "First":
        first_sequences = first_sequences.difference(numbers)
    elif command == "Remove" and sequences == "Second":
        second_sequences = second_sequences.difference(numbers)
    elif command == "Check" and sequences == "Subset":
        if first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences):
            print("True")
        else:
            print("False")

print(", ".join(str(el) for el in sorted(first_sequences)))
print(", ".join(str(el) for el in sorted(second_sequences)))

