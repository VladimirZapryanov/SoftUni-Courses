function smallestTwoNumber(array) {
    array.sort((a, b) => a - b);

    let smallestArray = [array[0], array[1]];
    console.log(smallestArray.join(' '));
}

smallestTwoNumber([30, 15, 50, 5])
smallestTwoNumber([3, 0, 10, 4, 7, 3])