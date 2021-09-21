income_in_bgn = float(input())
average_grade = float(input())
minimum_salary = float(input())
social_scholarship = 0
great_success_scholarship = 0
if income_in_bgn < minimum_salary and average_grade > 4.5:
    social_scholarship = minimum_salary * 0.35
if great_success_scholarship >= 5.5:
    great_success_scholarship = average_grade * 25
if great_success_scholarship < 5.5 and income_in_bgn > minimum_salary:
    print("You cannot get a scholarship!")
elif average_grade > 4.5 and income_in_bgn < minimum_salary:
    print(f"You get a Social scholarship {round(social_scholarship)} BGN")
elif average_grade > 5.5:
    print(f"You get a scholarship for excellent results {round(great_success_scholarship)} BGN")

