numbers = [int(num) for num in input().split()]
average_number = sum(numbers) / len(numbers)
top_five = []

for el in numbers:
    if el > average_number:
        top_five.append(el)
        top_five = sorted(top_five, reverse=True)

if len(top_five) <= 1:
    print("No")

elif len(top_five) >= 5:
    top_five = top_five[:5]
    print(" ".join(str(el) for el in top_five))

else:
    print(" ".join(str(el) for el in top_five))




