actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

total_points = academy_points
for j in range(number_of_judges):
    name_of_judge = input()
    judge_points = float(input())

    total_points += (len(name_of_judge) * judge_points) / 2
    if total_points > 1250.50:
        break

points_difference = 1250.50 - total_points
if total_points > 1250.50:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {points_difference:.1f} more!')
