function squareOfStars(count = 5) {

    let square = '';

    for(let i = 1; i <= count; i++) {
        for(let j = 1; j <= count; j++) {
            square += '* ';
        }
        square += '\n';
    }

    console.log(square);
}

squareOfStars(1)
squareOfStars(2)
squareOfStars(5)
squareOfStars()
squareOfStars(7)


