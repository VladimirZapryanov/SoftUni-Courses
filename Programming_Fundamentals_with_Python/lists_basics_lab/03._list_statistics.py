n = int(input())

positive = []
negative = []
count_positives = 0

for _ in range(n):
    number = int(input())
    if number > 0:
        positive.append(number)
        count_positives += 1
    else:
        negative.append(number)

sum_of_negatives = sum(negative)

print(positive)
print(negative)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")
