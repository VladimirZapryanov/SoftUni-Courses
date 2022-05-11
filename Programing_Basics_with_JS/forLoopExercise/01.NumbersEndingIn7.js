function numbersEndingInSeven() {
    let finalNumber = 1000;

    for (let i = 1; i <= finalNumber; i++) {
        if (i % 10 === 7) {
            console.log(i);
        }
    }
}

numbersEndingInSeven()