function number() {
    let firstNumber = 1;
    let lastNumber = 100;

    for(let number = firstNumber; number <= lastNumber; number++) {
        if(number % 3 === 0) {
            console.log(number);
        }
    }
}

number()