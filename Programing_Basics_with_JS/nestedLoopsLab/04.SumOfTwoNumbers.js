function sumOfTwoNumbers(input) {
    let startNumber = Number(input[0]);
    let endNumber = Number(input[1]);
    let magicNumber = Number(input[2]);

    let combinationCount = 0;
    let firstNumber = 0;
    let secondNumber = 0;
    let findCombination = false;

    for(let num1 = startNumber; num1 <= endNumber; num1++) {
        if(findCombination) {
            break;
        }
        for(let num2 = startNumber; num2 <= endNumber; num2++){
            combinationCount++;
            if(num1 + num2 === magicNumber) {
                firstNumber = num1;
                secondNumber = num2;
                findCombination = true;
                break;
            }
        }
    }
    if(findCombination) {
        console.log(`Combination N:${combinationCount} (${firstNumber} + ${secondNumber} = ${magicNumber})`);
    } else {
        console.log(`${combinationCount} combinations - neither equals ${magicNumber}`);
    }
}

sumOfTwoNumbers(["1",
"10",
"5"])

sumOfTwoNumbers(["23",
"24",
"20"])

sumOfTwoNumbers(["88",
"888",
"1000"])

sumOfTwoNumbers(["88", 
"888", 
"2000"])

