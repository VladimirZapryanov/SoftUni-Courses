function printElement(array, step) {
    let newArray = [];

    for (let i = 0; i < array.length; i += step) {
        newArray.push(array[i]);
    }

    return newArray;
}

console.log(printElement(['5',
    '20',
    '31',
    '4',
    '20'],
    2
))

console.log(printElement(['dsa',
    'asd',
    'test',
    'tset'],
    2
)
)
console.log(printElement(['1',
    '2',
    '3',
    '4',
    '5'],
    6
))