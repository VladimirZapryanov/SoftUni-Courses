function hospital(input) {
    let index = 0;
    let period = Number(input[index]);
    index++;
    let numbersOfDoctors = 7;

    let examinedPatients = 0;
    let notExaminedPatients = 0;
    let workingDays = 1;

    for (let i = 1; i <= period; i++) {
        let numberOfPaтients = Number(input[index]);
        index++;
        let patientsDiff = numberOfPaтients - numbersOfDoctors;

        if (workingDays % 3 === 0 && notExaminedPatients > examinedPatients) {
            numbersOfDoctors++;
        }

        if (numbersOfDoctors >= numberOfPaтients) {
            examinedPatients += numberOfPaтients;
        } else {
            examinedPatients += numbersOfDoctors;
            notExaminedPatients += numberOfPaтients - numbersOfDoctors;
        }

        workingDays++;
    }

    console.log(`Treated patients: ${examinedPatients}.`);
    console.log(`Untreated patients: ${notExaminedPatients}.`);
}

hospital(['4', '7', '27', '9', '1'])
hospital(['6', '25', '25', '25', '25', '25', '2'])