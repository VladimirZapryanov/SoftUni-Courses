function processOddPositions(array) {
    let oddArray = []

    for (let i = 0; i < array.length; i++) {
        if (i % 2 !== 0) {
            let number = Number(array[i]) * 2;
            oddArray.unshift(number);
        }
    }

    return oddArray.join(' ');
}

console.log(processOddPositions([10, 15, 20, 25]))
console.log(processOddPositions([3, 0, 10, 4, 7, 3]))