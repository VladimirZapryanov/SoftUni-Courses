// with one for - loop!!!

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


// with nested -loop!!!

function specialNumbers(input) {
    let number = Number(input[0]);

    let specialNumb = '';

    for(let n1 = 1; n1 <= 9; n1++) {
        for(let n2 = 1; n2 <= 9; n2++) {
            for(let n3 = 1; n3 <= 9; n3++) {
                for(let n4 = 1; n4 <= 9; n4++) {
                    if(number % n1 === 0 && number % n2 === 0 && number % n3 === 0 && number % n4 === 0) {
                        specialNumb += `${n1}${n2}${n3}${n4} `;
                    }
                }
            }
        }
    }

    console.log(specialNumb)
}

specialNumbers(['3'])
specialNumbers(['11'])
specialNumbers(['16'])