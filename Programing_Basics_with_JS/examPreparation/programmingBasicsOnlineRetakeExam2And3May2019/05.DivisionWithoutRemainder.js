function numbers(input) {
    let index = 0;
    let numbersCount = Number(input[index]);
    index++;

    let num1Count = 0;
    let num2Count = 0;
    let num3Count = 0;

    for(let num = 1; num <= numbersCount; num++) {
        let number = Number(input[index]);
        index++;
        if(number % 2 === 0) {
            num1Count++;
        }

        if(number % 3 === 0) {
            num2Count++;
        }

        if(number % 4 === 0) {
            num3Count++;
        }
    }

    let num1Percent = num1Count / numbersCount * 100;
    let num2Percent = num2Count / numbersCount * 100;
    let num3Percent = num3Count / numbersCount * 100;
    
    console.log(`${num1Percent.toFixed(2)}%`);
    console.log(`${num2Percent.toFixed(2)}%`);
    console.log(`${num3Percent.toFixed(2)}%`);
}

numbers(["10",
"680",
"2",
"600",
"200",
"800",
"799",
"199",
"46",
"128",
"65"])

numbers(["3",
"3",
"6",
"9"])
