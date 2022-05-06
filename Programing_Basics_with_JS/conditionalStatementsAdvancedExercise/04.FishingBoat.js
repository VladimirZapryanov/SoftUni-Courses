function fishingBoat(input) {
    let groupBudget = Number(input[0]);
    let season = input[1];
    let fishermanCount = Number(input[2]);

    let boatRent = 0;

    switch(season) {
        case 'Spring': boatRent = 3000; break;
        case 'Summer': 
        case 'Autumn': boatRent = 4200; break;
        case 'Winter': boatRent = 2600; break;
    }

    if (fishermanCount <= 6) {
        boatRent = boatRent * 0.9;
    } else if (fishermanCount <= 11) {
        boatRent = boatRent * 0.85;
    } else {
        boatRent = boatRent * 0.75;
    }

    if (fishermanCount % 2 == 0 && season !== 'Autumn') {
        boatRent = boatRent * 0.95;
    }

    let moneyDiff = Math.abs(groupBudget - boatRent);

    if (groupBudget >= boatRent) {
        console.log(`Yes! You have ${moneyDiff.toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${moneyDiff.toFixed(2)} leva.`);
    }
}

fishingBoat(["3000",
"Summer",
"11"])

fishingBoat(["3600",
"Autumn",
"6"])

fishingBoat(["2000",
"Winter",
"13"])
