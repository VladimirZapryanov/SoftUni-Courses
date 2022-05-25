function oddEvenPosition(input) {
    let index = 0;
    let numbersOfInputs = Number(input[index]);
    index++;

    let oddSum = 0;
    let oddMin = Number.MAX_SAFE_INTEGER;
    let oddMax = Number.MIN_SAFE_INTEGER;
    let evenSum = 0;
    let evenMin = Number.MAX_SAFE_INTEGER;
    let evenMax = Number.MIN_SAFE_INTEGER;

    for(let i = 1;  i<= numbersOfInputs; i++) {
        let number = Number(input[index]);
        index++;

        if(i % 2 === 1) {
            oddSum += number;
            if(oddMin > number) {
                oddMin = number;
            } 
            if (oddMax < number) {
                oddMax = number;
            }
        } else {
            evenSum += number;
            if(evenMin > number) {
                evenMin = number;
            } 
            if (evenMax < number) {
                evenMax = number;
            }
        }
    }

    console.log(`OddSum=${oddSum.toFixed(2)},`);

    if(oddMin === Number.MAX_SAFE_INTEGER) {
        console.log('OddMin=No,');
    } else {
        console.log(`OddMin=${oddMin.toFixed(2)},`);
    }
    
    if(oddMax === Number.MIN_SAFE_INTEGER) {
        console.log('OddMax=No,')
    } else {
        console.log(`OddMax=${oddMax.toFixed(2)},`);
    }
    
    console.log(`EvenSum=${evenSum.toFixed(2)},`);

    if(evenMin === Number.MAX_SAFE_INTEGER) {
        console.log('EvenMin=No,');
    } else {
        console.log(`EvenMin=${evenMin.toFixed(2)},`);
    }

    if(evenMax === Number.MIN_SAFE_INTEGER) {
        console.log('EvenMax=No');
    } else {
        console.log(`EvenMax=${evenMax.toFixed(2)}`);
    }
}

oddEvenPosition(['6', '2', '3', '5', '4', '2', '1'])
oddEvenPosition(['5', '3', '-2', '8', '11', '-3'])
oddEvenPosition(['2', '1.5', '-2.5'])
oddEvenPosition(['4', '1.5', '1.75', '1.5', '1.75'])
oddEvenPosition(['1', '1'])
oddEvenPosition(['1', '-5'])
oddEvenPosition(['0'])
oddEvenPosition(['3', '-1', '-2', '-3'])