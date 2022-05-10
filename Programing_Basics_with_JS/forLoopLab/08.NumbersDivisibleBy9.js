function numbers(input) {
    let firstNumber = Number(input[0]);
    let lastNumber = Number(input[1]);

    let sum = 0;
    let allNumbers = '';

    for (let i = firstNumber; i <= lastNumber; i++) {
        if (i % 9 === 0) {
            sum += i;
            allNumbers += `${i}\n`;
        }
    }
    
    console.log(`The sum: ${sum}`);
    console.log(allNumbers);
}

numbers(['100', '200'])