function averageNumber(input) {
    let index = 0;
    let allNumbersCount = Number(input[index]);
    index++;

    let sumOfNumbers = 0;

    for(let i = 1; i <= allNumbersCount; i++) {
        let number = Number(input[index]);
        index++;
        sumOfNumbers += number;
    }

    let averageNumber = sumOfNumbers / allNumbersCount;
    console.log(averageNumber.toFixed(2));
}

averageNumber(['4', '3', '2', '4', '2'])
averageNumber(['2', '6', '4'])
averageNumber(['3', '82', '43', '22'])
averageNumber(['4', '95', '23', '76', '23'])