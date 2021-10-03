name = input()
fail = 0
counter = 0
score = 0
while True:
    grade = float(input())
    score += grade
    counter +=1
    if grade <4:
        fail +=1
        if fail == 2:
            print(f"{name} has been excluded at {counter-1} grade")
            break
    if counter == 12:
        print(f"{name} graduated. Average grade: {score/counter:.2f}")
        break