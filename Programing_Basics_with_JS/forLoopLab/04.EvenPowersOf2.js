function evenPowers(input) {
    let number = Number(input[0]);

    for (let i = 0; i <= number; i++) {
        if (i % 2 === 0) {
            console.log(2**i);
        }
    }
}

evenPowers(['3'])
evenPowers(['4'])
evenPowers(['5'])
evenPowers(['6'])
evenPowers(['7'])