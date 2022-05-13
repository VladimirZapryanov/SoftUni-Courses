function grades(input) {
    let index = 0;
    let numbersOfStudents = Number(input[index]);
    index++;

    let failStudents = 0;
    let between3And4Students = 0;
    let between4And5Students = 0;
    let topStudents = 0;
    let allScore = 0;


    for (let i = 1; i <= numbersOfStudents; i++) {
        let studentScore = Number(input[index]);
        index++;

        if (studentScore < 3) {
            failStudents++;
            allScore += studentScore;
        } else if (studentScore < 4) {
            between3And4Students++;
            allScore += studentScore;
        } else if (studentScore < 5) {
            between4And5Students++;
            allScore += studentScore;
        } else {
            topStudents++;
            allScore += studentScore;
        }
    }

    let averageScore = allScore / numbersOfStudents;
    let failStudentsPercent = failStudents / numbersOfStudents * 100;
    let between3And4StudentsPercent = between3And4Students / numbersOfStudents * 100;
    let between4And5StudentsPercent = between4And5Students / numbersOfStudents * 100;
    let topStudentsPercent = topStudents / numbersOfStudents * 100;

    console.log(`Top students: ${topStudentsPercent.toFixed(2)}%`);
    console.log(`Between 4.00 and 4.99: ${between4And5StudentsPercent.toFixed(2)}%`);
    console.log(`Between 3.00 and 3.99: ${between3And4StudentsPercent.toFixed(2)}%`);
    console.log(`Fail: ${failStudentsPercent.toFixed(2)}%`);
    console.log(`Average: ${averageScore.toFixed(2)}`);
}

grades(['10' , '3.00', '2.99', '5.68', '3.01', '4', '4', '6', '4.50', '2.44', '5'])
grades(['6' , '2', '3', '4', '5', '6', '2.2'])