function uniquePinCodes(input) {
    let endOfFirstNumber = Number(input[0]);
    let endOfSecondNumber = Number(input[1]);
    let endOfThirdNumber = Number(input[2]);

    for(let num1 = 1; num1 <= endOfFirstNumber; num1++) {
        for(let num2 = 1; num2 <= endOfSecondNumber; num2++) {
            for(let num3 = 1; num3 <= endOfThirdNumber; num3++) {
                if(num1 % 2 === 0 && num3 % 2 === 0) {
                    let counter = 0;
                    for(let newNum = 1; newNum <= num2; newNum++) {
                        if(num2 % newNum === 0) {
                            counter++;
                        }
                    }
                    if(counter === 2) {
                        console.log(`${num1} ${num2} ${num3}`);
                    }
                }
            }
        }
    }
}

uniquePinCodes(['3', '5', '5'])