function operationsBetweenNumbers(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);
    let operation = input[2];

    let result = 0;
    let message = ''

    switch(operation) {    
        case '+': 
            type = '';
            result = firstNumber + secondNumber;
            if (result % 2 === 0) {
                type = 'even';
            } else {
                type = 'odd';
            }
            message = `${firstNumber} ${operation} ${secondNumber} = ${result} - ${type}`;
            break;

        case '-':
            type = '';
            result = firstNumber - secondNumber;
            if (result % 2 === 0) {
                type = 'even';
            } else {
                type = 'odd';
            }
            message = `${firstNumber} ${operation} ${secondNumber} = ${result} - ${type}`;
            break;

        case '*': 
            type = '';
            result = firstNumber * secondNumber; 
            if (result % 2 === 0) {
                type = 'even';
            } else {
                type = 'odd';
            }
            message = `${firstNumber} ${operation} ${secondNumber} = ${result} - ${type}`;
            break;
            
        case '/': 
            result = firstNumber / secondNumber;
            message = `${firstNumber} ${operation} ${secondNumber} = ${result.toFixed(2)}`;
            if (secondNumber === 0) {
                message = `Cannot divide ${firstNumber} by zero`;
            }
            break;
            
        case '%':
            result = firstNumber % secondNumber;
            message = `${firstNumber} ${operation} ${secondNumber} = ${result}`;
            if (secondNumber === 0) {
                message = `Cannot divide ${firstNumber} by zero`;
            }
            break;
    }

    console.log(message);
}

operationsBetweenNumbers(["10",
"12",
"+"])

operationsBetweenNumbers(["123",
"12",
"/"])

operationsBetweenNumbers(["112",
"0",
"/"])

operationsBetweenNumbers(["10",
"1",
"-"])

operationsBetweenNumbers(["10",
"3",
"%"])

operationsBetweenNumbers(["10",
"0",
"%"])

operationsBetweenNumbers(["7",
"3",
"*"])
