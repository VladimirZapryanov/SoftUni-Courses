function specialNumbers(input) {
    let number = Number(input[0]);

    let specialNumb = '';

    for(let num = 1111; num <= 9999; num++) {
        let numStr = num + "";
        let num1 = Number(numStr[0]);
        let num2 = Number(numStr[1]);
        let num3 = Number(numStr[2]);
        let num4 = Number(numStr[3]);

        if(number % num1 === 0 && number % num2 === 0 && number % num3 === 0 && number % num4 === 0) {
            specialNumb += `${num} `;
        }
    }

    console.log(specialNumb);
}

specialNumbers(['3'])
specialNumbers(['11'])
specialNumbers(['16'])