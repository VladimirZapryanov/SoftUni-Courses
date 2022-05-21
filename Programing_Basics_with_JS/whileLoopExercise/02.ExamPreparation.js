function examPreparation(input) {
    let index = 0;
    let numbersOfBadGrades = Number(input[index]);
    index++;

    let allProblemsCount = 0;
    let allGrades = 0;
    let badGrades = 0;
    let problemName = '';
    let needBreak = false;

    let command = input[index];
    index++;

    while(command !== 'Enough') {
        problemName = command;
        allProblemsCount++;
        let grade = Number(input[index]);
        index++;
        allGrades += grade;
        
        if(grade <= 4){
            badGrades++;
            if(badGrades === numbersOfBadGrades) {
                needBreak = true;
                break;
            }
        }

        command = input[index];
        index++;
    }

    let averageGrade = allGrades / allProblemsCount;

    if(needBreak) {
        console.log(`You need a break, ${badGrades} poor grades.`);
    } else {
        console.log(`Average score: ${averageGrade.toFixed(2)}`);
        console.log(`Number of problems: ${allProblemsCount}`);
        console.log(`Last problem: ${problemName}`);
    }
}

examPreparation(["3",
"Money",
"6",
"Story",
"4",
"Spring Time",
"5",
"Bus",
"6",
"Enough"])

examPreparation(["2",
"Income",
"3",
"Game Info",
"6",
"Best Player",
"4"])
