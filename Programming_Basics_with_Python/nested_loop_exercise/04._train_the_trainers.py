number_of_jury = int(input())
final_grade = 0
number_of_presentations = 0
command = input()
while command != "Finish":
    current_presentations_name = command
    number_of_presentations += 1
    current_presentations_grade = 0
    for presentation_grade in range(number_of_jury):
        grade = float(input())
        current_presentations_grade += grade
    presentation_average_grade = current_presentations_grade/number_of_jury
    final_grade += presentation_average_grade
    print(f'{current_presentations_name} - {presentation_average_grade:.2f}.')
    command = input()
final_average_grade = final_grade / number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")