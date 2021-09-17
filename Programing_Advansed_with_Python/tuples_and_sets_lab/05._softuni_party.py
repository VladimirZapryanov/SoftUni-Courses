def is_vip(guest):
    return guest[0].isdigit()


numbers_of_guests = int(input())
reservation_numbers = set()

for _ in range(numbers_of_guests):
    reservation = input()
    reservation_numbers.add(reservation)

arrived_guests = input()
while not arrived_guests == "END":
    reservation_numbers.remove(arrived_guests)
    arrived_guests = input()

vip_guests = sorted([g for g in reservation_numbers if is_vip(g)])
regular_guests = sorted([g for g in reservation_numbers if not is_vip(g)])

print(len(reservation_numbers))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]

