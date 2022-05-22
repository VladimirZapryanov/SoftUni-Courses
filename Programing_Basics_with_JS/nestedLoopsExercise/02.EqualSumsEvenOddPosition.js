function equalSumsEvenOddPosition(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);

    let result = '';

    for(let num = firstNumber; num <= secondNumber; num++) {
        let strNum = num + "";

        let oddSum = Number(strNum[0]) + Number(strNum[2]) + Number(strNum[4]);
        let evenSum = Number(strNum[1]) + Number(strNum[3]) + Number(strNum[5]);


        if(oddSum === evenSum) {
            result += `${num} `;
        }
    }

    console.log(result);
}

equalSumsEvenOddPosition(['100000', '100050'])
equalSumsEvenOddPosition(['123456', '124000'])
equalSumsEvenOddPosition(['299900', '300000'])
equalSumsEvenOddPosition(['100115', '100120'])