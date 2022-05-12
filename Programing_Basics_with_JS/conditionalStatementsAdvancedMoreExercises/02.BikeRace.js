function bikeRace(input) {
    let juniorsCount = Number(input[0]);
    let seniorsCount = Number(input[1]);
    let typeOfRoad = input[2];

    let money = 0;

    switch(typeOfRoad) {
        case 'trail': money = juniorsCount * 5.50 + seniorsCount * 7; break;
        case 'cross-country':
            if (juniorsCount + seniorsCount >= 50) {
                money = juniorsCount * (8 * 0.75) + seniorsCount * (9.50 * 0.75);
            } else {
                money = juniorsCount * 8 + seniorsCount * 9.50;
            } break;
        case 'downhill': money = juniorsCount * 12.25 + seniorsCount * 13.75; break;
        case 'road': money = juniorsCount * 20 + seniorsCount * 21.50; break;
    }

    let moneyAfterTaxes = money * 0.95;

    console.log(moneyAfterTaxes.toFixed(2));
}

bikeRace(['10', '20', 'trail'])
bikeRace(['21', '26', 'cross-country'])
bikeRace(['10', '10', 'downhill'])
bikeRace(['3', '40', 'road'])