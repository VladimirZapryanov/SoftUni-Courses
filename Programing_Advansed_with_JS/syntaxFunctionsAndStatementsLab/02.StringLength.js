function stringLength(arg1, arg2, arg3) {
    let firstString = arg1;
    let secondString = arg2;
    let thirdString = arg3;

    let sumOfStringLength = firstString.length + secondString.length + thirdString.length;
    let averageStringLength = sumOfStringLength / 3;

    console.log(Math.floor(sumOfStringLength));
    console.log(Math.floor(averageStringLength));
}

stringLength('chocolate', 'ice cream', 'cake')
stringLength('pasta', '5', '22.3')
