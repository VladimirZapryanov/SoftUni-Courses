function sumFirtstLast(array) {
    let first = Number(array.shift());
    let last = Number(array.pop());

    let sum = first + last;
    return sum;
}

console.log(sumFirtstLast(['20', '30', '40']))
console.log(sumFirtstLast(['5', '10']))