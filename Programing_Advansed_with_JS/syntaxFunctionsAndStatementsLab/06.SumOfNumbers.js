function sumOfNumbers(num1, num2) {
    let firstNumber = Number(num1);
    let secondNumber = Number(num2);

    let result = 0;;
    
    for(let i = firstNumber; i <= secondNumber; i++) {
        result += i;
    }

    return result;
}

sumOfNumbers('1', '5')
sumOfNumbers('-8', '20')