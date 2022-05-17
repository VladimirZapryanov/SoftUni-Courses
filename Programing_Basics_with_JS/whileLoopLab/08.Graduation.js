function graduation(input) {
    let index = 0;
    let name = input[index];
    index++;

    let classCount = 0;
    let failClass = 0;
    let yearScore = 0;
    let graduated = false;

    while(failClass < 1) {
        let score = Number(input[index]);
        yearScore += score
        if (score < 4) {
            failClass++;
        } 

        classCount++;
        index++;

        if (classCount === 12) {
            graduated = true;
            break;
        }
    }
    
    let avgScore = yearScore / classCount;

    if (graduated) {
        console.log(`${name} graduated. Average grade: ${avgScore.toFixed(2)}`);
    } else {
        console.log(`${name} has been excluded at ${classCount} grade`);
    }
}
    

graduation(["Gosho", 
"5",
"5.5",
"6",
"5.43",
"5.5",
"6",
"5.55",
"5",
"6",
"6",
"5.43",
"5"])


graduation(["Mimi", 
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"])
