function sumFirtstLast(array) {
    let first = Number(array.shift());
    let last = Number(array.pop());

    let sum = first + last;
    console.log(sum);
}

sumFirtstLast(['20', '30', '40'])
sumFirtstLast(['5', '10'])