function fitnessCard(input) {
    let budget = Number(input[0]);
    let gender = input[1];
    let age = Number(input[2]);
    let typeOfSport = input[3];

    let cardPrice = 0;

    switch(gender) {
        case 'm':
            switch(typeOfSport) {
                case 'Gym': cardPrice = 42; break;
                case 'Boxing': cardPrice = 41; break;
                case 'Yoga': cardPrice = 45; break;
                case 'Zumba': cardPrice = 34; break;
                case 'Dances': cardPrice = 51; break;
                case 'Pilates': cardPrice = 39; break;
            } break;
        case 'f':
            switch(typeOfSport) {
                case 'Gym': cardPrice = 35; break;
                case 'Boxing': cardPrice = 37; break;
                case 'Yoga': cardPrice = 42; break;
                case 'Zumba': cardPrice = 31; break;
                case 'Dances': cardPrice = 53; break;
                case 'Pilates': cardPrice = 37; break;
            } break;
    }

    if(age <= 19) {
        cardPrice = cardPrice * 0.80;
    }

    if(budget >= cardPrice) {
        console.log(`You purchased a 1 month pass for ${typeOfSport}.`);
    } else {
        let moneyDiff = cardPrice - budget;
        console.log(`You don't have enough money! You need $${moneyDiff.toFixed(2)} more.`);
    }
}

fitnessCard(["50",
"m",
"23",
"Gym"])

fitnessCard(["20",
"f",
"15",
"Yoga"])

fitnessCard(["10",
"m",
"50",
"Pilates"])
