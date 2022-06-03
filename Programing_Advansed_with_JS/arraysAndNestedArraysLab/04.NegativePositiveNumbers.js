function negativePositiveNumbers(array) {
    let result = [];

    for (let element of array) {
        if (element >= 0) {
            result.push(element);
        } else {
            result.unshift(element);
        }
    }

    console.log(result.join('\n'));
}

negativePositiveNumbers([7, -2, 8, 9])
negativePositiveNumbers([3, -2, 0, -1])