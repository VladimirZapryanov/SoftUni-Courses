function numberPyramid(input) {
    let number = Number(input[0]);

    let current = 1;
    let isBigger = false;
    let currentLine = '';

    for(let num1 = 1; num1 <= number; num1++) {
        for(let num2 = 1; num2 <= num1; num2++){
            if (current > number) {
                isBigger = true;
                break;
            }

            currentLine += current + " ";
            current++;
        }

        console.log(currentLine);
        currentLine = '';
        if(isBigger) {
            break;
        }
       
    }
}

numberPyramid(['7'])
numberPyramid(['12'])
numberPyramid(['15'])