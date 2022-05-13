function backToThePast(input) {
    let money = Number(input[0]);
    let year = Number(input[1]);

    let neededMoney = 0;
    let age = 18;

    for (let i = 1800; i <= year; i++) {
        if (i % 2 == 0) {
            neededMoney += 12000;
            age ++;
        } else {
            neededMoney += 12000 + 50 * age;
            age++;
        }
    }

    let moneyDiff = Math.abs(money - neededMoney);

    if (money >= neededMoney) {
        console.log(`Yes! He will live a carefree life and will have ${moneyDiff.toFixed(2)} dollars left.`);
    } else {
        console.log(`He will need ${moneyDiff.toFixed(2)} dollars to survive.`);
    }
}

backToThePast(['50000', '1802'])
backToThePast(['100000.15', '1808'])