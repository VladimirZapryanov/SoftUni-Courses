function flowers(input) {
    let numbersOfChrysanthemums = Number(input[0]);
    let numbersOfRoses = Number(input[1]);
    let numbersOfTulips = Number(input[2]);
    let season = input[3];
    let isItHoliday = input[4];

    let allFlowerCount = numbersOfChrysanthemums + numbersOfRoses + numbersOfTulips;
    let priceForFlowers = 0;
    let arrangingPrice = 2;

    switch(season) {
        case 'Summer':
        case 'Spring': 
            if (isItHoliday === 'Y') {
                priceForFlowers = numbersOfChrysanthemums * (2.00 * 1.15) + numbersOfRoses * (4.10 * 1.15) + numbersOfTulips * (2.50 * 1.15);
            } else {
                priceForFlowers = numbersOfChrysanthemums * 2.00 + numbersOfRoses * 4.10 + numbersOfTulips * 2.50;
            }
            
            if (season === 'Spring' && numbersOfTulips > 7) {
                priceForFlowers = priceForFlowers * 0.95;
            } break;
        case 'Autumn':
        case 'Winter':
            if (isItHoliday === 'Y') {
                priceForFlowers = numbersOfChrysanthemums * (3.75 * 1.15) + numbersOfRoses * (4.50 * 1.15) + numbersOfTulips * (4.15 * 1.15);
            } else {
                priceForFlowers = numbersOfChrysanthemums * 3.75 + numbersOfRoses * 4.50 + numbersOfTulips * 4.15;
            }
            
            if (season === 'Winter' && numbersOfRoses >= 10) {
                priceForFlowers = priceForFlowers * 0.90;
            } break;
    }

    if (allFlowerCount > 20) {
        priceForFlowers = priceForFlowers * 0.80;
    }

    priceForFlowers += arrangingPrice;

    console.log(priceForFlowers.toFixed(2));
}

flowers(['2', '4', '8', 'Spring', 'Y'])
flowers(['3', '10', '9', 'Winter', 'N'])
flowers(['10', '10', '10', 'Autumn', 'N'])