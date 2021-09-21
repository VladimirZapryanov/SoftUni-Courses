score = int(input())
extra_bonus_score = 0
if score <= 100:
    bonus_score = 5
elif 1000 > score > 100:
    bonus_score = score * 0.2
else:
    bonus_score = score * 0.1
if score % 2 == 0:
    extra_bonus_score = 1
elif score % 10 == 5:
    extra_bonus_score = 2
total_bonus_score = bonus_score + extra_bonus_score
total_score = score + bonus_score + extra_bonus_score
print(total_bonus_score)
print(total_score)