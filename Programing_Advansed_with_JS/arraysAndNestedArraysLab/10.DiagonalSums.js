function diagonalSums(matrix) {
    let primarySum = 0;
    let secondarySum = 0;

    const length = matrix.length;

    for (let row = 0; row < length; row++) {
        primarySum += matrix[row][row];
    }


   for (let row = 0; row < length; row++) {
       secondarySum += matrix[length - 1 - row][row];
   }

    console.log(`${primarySum} ${secondarySum}`);
}

diagonalSums([[20, 40],
[10, 60]]
)

diagonalSums([[3, 5, 17],
[-1, 7, 14],
[1, -8, 89]]
)