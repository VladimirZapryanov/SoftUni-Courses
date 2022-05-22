function multiplicationTable() {

    for(let firstNumber = 1; firstNumber <= 10; firstNumber++) {
        for(let secondNumber = 1; secondNumber <= 10; secondNumber++) {
            let result = firstNumber * secondNumber;
            console.log(`${firstNumber} * ${secondNumber} = ${result}`);
        }
    }
}

multiplicationTable()