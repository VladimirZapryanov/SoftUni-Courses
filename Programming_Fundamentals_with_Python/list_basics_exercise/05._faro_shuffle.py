cards = input().split()
n = int(input())

half_size = len(cards) // 2

for i in range(n):

    left_side = cards[:half_size]
    right_side = cards[half_size:]

    faro_cards = []

    for j in range(len(left_side)):
        faro_cards.append(left_side[j])
        faro_cards.append(right_side[j])

    cards = faro_cards

print(cards)