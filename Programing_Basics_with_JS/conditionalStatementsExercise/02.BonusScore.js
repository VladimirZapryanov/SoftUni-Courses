function bonusScore(input) {
    let number = Number(input[0]);

    let bonusPoint = 0;

    if (number <= 100) {
        bonusPoint += 5;
    } else if (number > 100 && number < 1000) {
        bonusPoint += number * 0.2;
    } else {
        bonusPoint += number * 0.1;
    }

    if (number % 2 === 0) {
        bonusPoint += 1;
    } else if (number % 10 === 5) {
        bonusPoint += 2;
    }

    console.log(bonusPoint);
    console.log(bonusPoint + number);
}

bonusScore(["20"])
bonusScore(["175"])
bonusScore(["2703"])
bonusScore(["15875"])