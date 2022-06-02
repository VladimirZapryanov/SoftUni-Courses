function sameNumbers(number) {
    let strNumber = String(number);
    let firstNum = Number(strNumber[0]);
    let lengthOfNumbers = strNumber.length;

    let sumOfNumbers = 0;
    let numIsSame = true;

    for(let i = 0; i < lengthOfNumbers; i++) {
        let currentNum = Number(strNumber[i]);
        sumOfNumbers += currentNum;

        if(firstNum !== currentNum) {
            numIsSame = false;
        }
    }

    if(numIsSame) {
        console.log('true');
    } else {
        console.log('false');
    }

    console.log(sumOfNumbers);
}

sameNumbers(22222222)
sameNumbers(1234)