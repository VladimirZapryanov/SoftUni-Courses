function addBags(input) {
    let luggagePriceMoreOf20kg = Number(input[0]);
    let luggageKilograms = Number(input[1]);
    let daysToGoAway = Number(input[2]);
    let luggageCount = Number(input[3]);

    let luggagePriceTo10kg = luggagePriceMoreOf20kg * 0.2;
    let luggagePriceTo20kg = luggagePriceMoreOf20kg * 0.5;
    let finalLuggagePrice = 0;

    if(luggageKilograms < 10) {
        finalLuggagePrice = luggagePriceTo10kg;
    } else if (luggageKilograms >= 10 && luggageKilograms <= 20) {
        finalLuggagePrice = luggagePriceTo20kg;
    } else if (luggageKilograms > 20) {
        finalLuggagePrice = luggagePriceMoreOf20kg;
    }

    if(daysToGoAway > 30) {
        finalLuggagePrice += finalLuggagePrice * 0.1;
    } else if (daysToGoAway >= 7 && daysToGoAway <= 30) {
        finalLuggagePrice += finalLuggagePrice * 0.15;
    } else if (daysToGoAway < 7) {
        finalLuggagePrice += finalLuggagePrice * 0.4;
    }

    finalLuggagePrice = finalLuggagePrice * luggageCount;

    console.log(`The total price of bags is: ${finalLuggagePrice.toFixed(2)} lv.`);
}

addBags(["30",
"18",
"15",
"2"])

addBags(["25.50",
"5",
"36",
"6"])

addBags(["63.80",
"23",
"3",
"1"])

