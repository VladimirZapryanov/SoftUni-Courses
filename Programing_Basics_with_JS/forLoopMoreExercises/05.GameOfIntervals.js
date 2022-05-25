function gameOfIntervals(input) {
    let index = 0;
    let numberOfMoves = Number(input[index]);
    index++;

    let totalScore = 0;
    let numberToTen = 0;
    let numberToTwenty = 0;
    let numberToThirty = 0;
    let numberToForty = 0;
    let numberToFifty = 0;
    let invalidNumber = 0;

    for(let i = 1; i <= numberOfMoves; i++) {
        let number = Number(input[index]);
        index++;

        if(number >= 0 && number <= 9) {
            totalScore += number * 0.2;
            numberToTen++;
        } else if (number >= 10 && number <= 19) {
            totalScore += number * 0.3;
            numberToTwenty++;
        } else if (number >= 20 && number <= 29) {
            totalScore += number * 0.4;
            numberToThirty++;
        } else if (number >= 30 && number <= 39) {
            totalScore += 50;
            numberToForty++;
        } else if (number >= 40 && number <= 50) {
            totalScore += 100;
            numberToFifty++;
        } else {
            totalScore = totalScore / 2;
            invalidNumber++;
        }
    }

    let numberToTenPercent = numberToTen / numberOfMoves * 100;
    let numberToTwentyPercent = numberToTwenty / numberOfMoves * 100;
    let numberToThirtyPercent = numberToThirty / numberOfMoves * 100;
    let numberToFortyPercent = numberToForty / numberOfMoves * 100;
    let numberToFiftyPercent = numberToFifty / numberOfMoves * 100;
    let invalidNumberPercent = invalidNumber / numberOfMoves * 100;

    console.log(totalScore.toFixed(2));
    console.log(`From 0 to 9: ${numberToTenPercent.toFixed(2)}%`);
    console.log(`From 10 to 19: ${numberToTwentyPercent.toFixed(2)}%`);
    console.log(`From 20 to 29: ${numberToThirtyPercent.toFixed(2)}%`);
    console.log(`From 30 to 39: ${numberToFortyPercent.toFixed(2)}%`);
    console.log(`From 40 to 50: ${numberToFiftyPercent.toFixed(2)}%`);
    console.log(`Invalid numbers: ${invalidNumberPercent.toFixed(2)}%`);
}

gameOfIntervals(['10', '43', '57', '-12', '23', '12', '0', '50', '40', '30', '20'])