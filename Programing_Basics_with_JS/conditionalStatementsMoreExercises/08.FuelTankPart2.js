function fuelTank(input) {
    let typeOfFuel = input[0];
    let fuelAmount = Number(input[1]);
    let discountCard = input[2];

    let gasolinePricePerLiter = 2.22;
    let dieselPricePerLiter = 2.33;
    let gasPricePerLiter = 0.93;

    let priceForFuel = 0;

    switch(typeOfFuel) {
        case 'Gasoline': 
            if (discountCard === 'Yes') {
                gasolinePricePerLiter -= 0.18;
                priceForFuel = gasolinePricePerLiter * fuelAmount; 
            } else {
                priceForFuel = gasolinePricePerLiter * fuelAmount;
            } 
            break;
        case 'Diesel': 
            if (discountCard === 'Yes') {
                dieselPricePerLiter -= 0.12;
                priceForFuel = dieselPricePerLiter * fuelAmount; 
            } else {
                priceForFuel = dieselPricePerLiter * fuelAmount; 
            }
            break;
        case 'Gas': 
            if (discountCard === 'Yes') {
                gasPricePerLiter -= 0.08;
                priceForFuel = gasPricePerLiter * fuelAmount; 
            } else {
                priceForFuel = gasPricePerLiter * fuelAmount; 
            } 
            break;
    }

    if (fuelAmount >= 20 && fuelAmount <= 25) {
        priceForFuel = priceForFuel * 0.92;
    } else if (fuelAmount > 25) {
        priceForFuel = priceForFuel * 0.90;
    }

    console.log(`${priceForFuel.toFixed(2)} lv.`)
}

fuelTank(['Gas', '30', 'Yes'])
fuelTank(['Gasoline', '25', 'No'])
fuelTank(['Diesel', '19', 'No'])
   