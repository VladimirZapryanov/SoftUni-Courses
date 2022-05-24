function trainTheTrainers(input) {
    let index = 0;
    let numbersOfJury = Number(input[index]);
    index++;
    let command = input[index];
    index++;

    let presentationCount = 0;
    let presentationTotalGrade = 0;

    while(command !== 'Finish') {
        let presentationName = command;
        presentationCount++;
        let courseTotalGrade = 0;

        for(let n = 1; n <= numbersOfJury; n++) {
            let courseGrade = Number(input[index]);
            index++;
            courseTotalGrade += courseGrade;
        }

        let courseAverageGrade = courseTotalGrade / numbersOfJury;
        presentationTotalGrade += courseAverageGrade;
        console.log(`${presentationName} - ${courseAverageGrade.toFixed(2)}.`);

        command = input[index];
        index++;
    }

    let presentationAverageGrade = presentationTotalGrade / presentationCount;
    console.log(`Student's final assessment is ${presentationAverageGrade.toFixed(2)}.`);
}

trainTheTrainers(["2",
"While-Loop",
"6.00",
"5.50",
"For-Loop",
"5.84",
"5.66",
"Finish"])


trainTheTrainers(["3",
"Arrays",
"4.53",
"5.23",
"5.00",
"Lists",
"5.83",
"6.00",
"5.42",
"Finish"])

trainTheTrainers(["2",
"Objects and Classes",
"5.77",
"4.23",
"Dictionaries",
"4.62",
"5.02",
"RegEx",
"2.88",
"3.42",
"Finish"])


