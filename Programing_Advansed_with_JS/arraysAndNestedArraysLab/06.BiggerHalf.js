function biggerHalf(array) {
    array.sort((a,b) => a - b);

    let halfArray = [];
    let arrayLength = array.length;

    for (let i = Math.floor(arrayLength / 2); i < arrayLength; i++) {
        halfArray.push(array[i]);
    }

    return halfArray;
}

console.log(biggerHalf([4, 7, 2, 5]))
console.log(biggerHalf([3, 19, 14, 7, 2, 19, 6]))