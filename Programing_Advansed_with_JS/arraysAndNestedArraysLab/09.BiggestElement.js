function biggestElement(matrix) {
    let biggestNumber = Number.MIN_SAFE_INTEGER;
    
    for (let row of matrix) {
        for (let colElement of row) {
            if (colElement > biggestNumber) {
                biggestNumber = colElement;
            }
        }
    }
    return biggestNumber;
}

console.log(biggestElement([[20, 50, 10],
[8, 33, 145]]
))

console.log(biggestElement([[3, 5, 7, 12],
[-1, 4, 33, 2],
[8, 3, 0, 4]]
))