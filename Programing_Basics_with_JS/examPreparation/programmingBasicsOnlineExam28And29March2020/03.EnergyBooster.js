function energyBooster(input) {
    let typeOfFruit = input[0];
    let typeOfSet = input[1];
    let numbersOfSet = Number(input[2]);

    let setPrice = 0;
    let allCost = 0;

    switch(typeOfSet) {
        case 'small':
            switch(typeOfFruit) {
                case 'Watermelon':
                    setPrice = 56 * 2;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Mango':
                    setPrice = 36.66 * 2;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Pineapple':
                    setPrice = 42.10 * 2;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Raspberry':
                    setPrice = 20 * 2;
                    allCost = setPrice * numbersOfSet;
                    break;
            } break;
        
        case 'big':
            switch(typeOfFruit) {
                case 'Watermelon':
                    setPrice = 28.70 * 5;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Mango':
                    setPrice = 19.60 * 5;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Pineapple':
                    setPrice = 24.80 * 5;
                    allCost = setPrice * numbersOfSet;
                    break;
                case 'Raspberry':
                    setPrice = 15.20 * 5;
                    allCost = setPrice * numbersOfSet;
                    break;
            } break;
    }

    if(allCost >= 400 && allCost <= 1000) {
        allCost = allCost * 0.85;
    } else if (allCost > 1000) {
        allCost = allCost * 0.5;
    }

    console.log(`${allCost.toFixed(2)} lv.`);
}

energyBooster(["Watermelon",
"big",
"4"])

energyBooster(["Pineapple",
"small",
"1"])

energyBooster(["Raspberry",
"small",
"50"])

energyBooster(["Mango",
"big",
"8"])
