days = int(input())

treated_patient = 0
untreated_patient = 0
doctors = 7

for day in range(1, days + 1):
    patients = int(input())

    if day % 3 == 0:
        if untreated_patient > treated_patient:
            doctors += 1

    if patients > doctors:
        untreated_patient += patients - doctors
        treated_patient += doctors
    else:
        treated_patient += patients

print(f'Treated patients: {treated_patient}.')
print(f'Untreated patients: {untreated_patient}.')



