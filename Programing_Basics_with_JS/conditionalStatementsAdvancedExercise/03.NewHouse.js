function newHouse(input) {
    let typeOfFlowers = input[0];
    let flowersCount = Number(input[1]);
    let budget = Number(input[2]);

    let rosePrice = 5;
    let dahliaPrice = 3.80;
    let tulipPrice = 2.80;
    let narcissusPrice = 3;
    let gladiolusPrice = 2.50;

    let finalPriceForFlowers = 0;
    let consoleMessege = '';

    switch(typeOfFlowers) {
        case 'Roses': finalPriceForFlowers = flowersCount * rosePrice;
            if (flowersCount > 80) {
                finalPriceForFlowers = finalPriceForFlowers * 0.9;
            }; 
            break;
        case 'Dahlias': finalPriceForFlowers = flowersCount * dahliaPrice; 
            if (flowersCount > 90) {
                finalPriceForFlowers = finalPriceForFlowers * 0.85;
            };
            break;
        case 'Tulips': finalPriceForFlowers = flowersCount * tulipPrice; 
            if (flowersCount > 80) {
                finalPriceForFlowers = finalPriceForFlowers * 0.85;
            };
            break;
        case 'Narcissus': finalPriceForFlowers = flowersCount * narcissusPrice; 
            if (flowersCount < 120) {
                finalPriceForFlowers = finalPriceForFlowers * 1.15;
            };
            break;
        case 'Gladiolus': finalPriceForFlowers = flowersCount * gladiolusPrice; 
            if (flowersCount < 80) {
                finalPriceForFlowers = finalPriceForFlowers * 1.20;
            };
            break;
    };

    let moneyDiff = Math.abs(budget - finalPriceForFlowers);

    if (budget >= finalPriceForFlowers) {
        consoleMessege = `Hey, you have a great garden with ${flowersCount} ${typeOfFlowers} and ${moneyDiff.toFixed(2)} leva left.`;
    } else {
        consoleMessege = `Not enough money, you need ${moneyDiff.toFixed(2)} leva more.`;
    }

    console.log(consoleMessege);
}

newHouse(["Roses",
"55",
"250"])

newHouse(["Tulips",
"88",
"260"])

newHouse(["Narcissus",
"119",
"360"])
