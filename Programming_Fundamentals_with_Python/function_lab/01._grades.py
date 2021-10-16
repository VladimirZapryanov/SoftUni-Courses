def grades(score):

    if 2 <= score <= 2.99:
        return "Fail"
    elif 3 <= score <= 3.49:
        return "Poor"
    elif 3.50 <= score <= 4.49:
        return "Good"
    elif 4.50 <= score <= 5.49:
        return "Very Good"
    elif 5.50 <= score <= 6.00:
        return "Excellent"


grade = float(input())
print(grades(grade))

