function greaterNumber(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);

    if (firstNumber > secondNumber) {
        console.log(firstNumber);
    }else {
        console.log(secondNumber);
    }
}

greaterNumber(["5", "3"])
greaterNumber(["3", "5"])
greaterNumber(["10", "10"])
greaterNumber(["-5", "5"])