function safari(input) {
    let budget = Number(input[0]);
    let neededFuel = Number(input[1]);
    let dayOfWeek = input[2];

    let gitPrice = 100;
    let fuelPricePerLitter = 2.10;

    let totalNeededMoney = neededFuel * fuelPricePerLitter + gitPrice;

    if(dayOfWeek === 'Saturday') {
        totalNeededMoney = totalNeededMoney * 0.9;
    } else if (dayOfWeek === 'Sunday') {
        totalNeededMoney = totalNeededMoney * 0.8;
    }

    let moneyDiff = Math.abs(budget - totalNeededMoney);

    if(budget >= totalNeededMoney) {
        console.log(`Safari time! Money left: ${moneyDiff.toFixed(2)} lv. `);
    } else {
        console.log(`Not enough money! Money needed: ${moneyDiff.toFixed(2)} lv.`);
    }
}

safari(['1000', '10', 'Sunday'])
safari(['120', '30', 'Saturday'])