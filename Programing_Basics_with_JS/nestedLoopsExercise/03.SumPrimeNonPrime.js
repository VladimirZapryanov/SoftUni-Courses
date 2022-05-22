function sumPrimeNonPrime(input) {
    let index = 0;
    let command = input[index];
    index++;

    let primeSum = 0;
    let nonPrimeSum = 0;

    while(command !== 'stop') {
        let number = Number(command);

        if(number < 0) {
            console.log('Number is negative.');
            command = input[index];
            index++;
            continue;
        }

        if(number === 1) {
            primeSum += number;
            command = input[index];
            index++;
            continue;
        }
        
        let isPrime = true;
        for(let i = 2; i < Math.sqrt(number); i++) {
            if(number % i === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            primeSum += number;
        } else {
            nonPrimeSum += number;
        }

        command = input[index];
        index++;
    }

    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}

sumPrimeNonPrime(["3",
"9",
"0",
"7",
"19",
"4",
"stop"])

sumPrimeNonPrime(["30",
"83",
"33",
"-1",
"20",
"stop"])

sumPrimeNonPrime(["0",
"-9",
"0",
"stop"])


