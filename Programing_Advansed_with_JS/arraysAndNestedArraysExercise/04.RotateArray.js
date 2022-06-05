function rotateArray(array, amountOfRotation) {

    if (amountOfRotation % array.length === 0) {
        array = array;
    } else {
        for (let i = 0; i < amountOfRotation; i++) {
            array.unshift(array.pop());
        }
    }

    console.log(array.join(' '));
}

rotateArray(['1',
    '2',
    '3',
    '4'],
    2
)

rotateArray(['Banana',
    'Orange',
    'Coconut',
    'Apple'],
    15
)