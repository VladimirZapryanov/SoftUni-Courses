<<<<<<< HEAD
needed_experience = float(input())
numbers_of_battles = int(input())
experience_earned_per_battle = float(input())

count_of_battle = 0
he_is_fail = True

while needed_experience > 0:
    needed_experience -= experience_earned_per_battle
    count_of_battle += 1
    if count_of_battle % 3 == 0:
        needed_experience -= experience_earned_per_battle * 0.15
    if count_of_battle % 5 == 0:
        needed_experience += experience_earned_per_battle * 0.10
    if count_of_battle % 15 == 0:
        needed_experience -= experience_earned_per_battle * 0.05
    if needed_experience <= 0:
        print(f"Player successfully collected his needed experience for {count_of_battle} battles.")
        he_is_fail = False
        break
    experience_earned_per_battle = float(input())

if he_is_fail:
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed")
=======
needed_experience = float(input())
numbers_of_battles = int(input())
experience_earned_per_battle = float(input())

count_of_battle = 0
he_is_fail = True

while needed_experience > 0:
    needed_experience -= experience_earned_per_battle
    count_of_battle += 1
    if count_of_battle % 3 == 0:
        needed_experience -= experience_earned_per_battle * 0.15
    if count_of_battle % 5 == 0:
        needed_experience += experience_earned_per_battle * 0.10
    if count_of_battle % 15 == 0:
        needed_experience -= experience_earned_per_battle * 0.05
    if needed_experience <= 0:
        print(f"Player successfully collected his needed experience for {count_of_battle} battles.")
        he_is_fail = False
        break
    experience_earned_per_battle = float(input())

if he_is_fail:
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed")
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
