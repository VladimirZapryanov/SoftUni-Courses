function accountBalance(input) {
    let index = 0;

    let data = input[index];
    index++;

    let totalSum = 0;

    while(data !== 'NoMoreMoney') {
        let sum = Number(data);

        if (sum < 0) {
            console.log('Invalid operation!');
            break;
        }
        totalSum += sum;
        console.log(`Increase: ${sum.toFixed(2)}`);
        data = input[index];
        index++;
    }

    console.log(`Total: ${totalSum.toFixed(2)}`);
}

accountBalance(["5.51", 
"69.42",
"100",
"NoMoreMoney"])


accountBalance(["120",
"45.55",
"-150"])
