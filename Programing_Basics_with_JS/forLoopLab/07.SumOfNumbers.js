function sumOfNumbers(input) {
    let number = input[0];

    let sum = 0;
    let numberLength = number.length;

    for (let i = 0; i < numberLength; i++) {
        sum += Number(number[i]);
    }

    console.log(`The sum of the digits is:${sum}`)
}

sumOfNumbers(['1234'])
sumOfNumbers(['564891'])