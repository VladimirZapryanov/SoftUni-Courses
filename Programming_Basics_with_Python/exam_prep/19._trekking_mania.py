group_count = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(group_count):
    people_count = int(input())
    if people_count <= 5:
        musala += people_count
        total_people += people_count
    elif 6 <= people_count <= 12:
        mont_blanc += people_count
        total_people += people_count
    elif 13 <= people_count <= 25:
        kilimanjaro += people_count
        total_people += people_count
    elif 26 <= people_count <= 40:
        k2 += people_count
        total_people += people_count
    elif people_count >= 41:
        everest += people_count
        total_people += people_count

print(f"{((musala / total_people) * 100):.2f}%")
print(f"{((mont_blanc / total_people) * 100):.2f}%")
print(f"{((kilimanjaro / total_people) * 100):.2f}%")
print(f"{((k2 / total_people) * 100):.2f}%")
print(f"{((everest / total_people) * 100):.2f}%")
