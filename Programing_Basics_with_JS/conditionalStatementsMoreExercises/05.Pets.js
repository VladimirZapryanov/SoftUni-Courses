function pets(input) {
    let numbersOfDays = Number(input[0]);
    let foodInKilograms = Number(input[1]);
    let dogFoodPerDayKilograms = Number(input[2]);
    let catFoodPerDayKilograms = Number(input[3]);
    let turtleFoodPerDayGrams = Number(input[4]);

    let turtleFoodPerDayKilograms = turtleFoodPerDayGrams / 1000;
    let allEatenFoodPerDay = dogFoodPerDayKilograms + catFoodPerDayKilograms + turtleFoodPerDayKilograms;
    let allEatenFood = allEatenFoodPerDay * numbersOfDays;
    let foodDiff = Math.abs(allEatenFood - foodInKilograms);
    
    if (foodInKilograms >= allEatenFood) {
        console.log(`${Math.floor(foodDiff)} kilos of food left.`);
    } else {
        console.log(`${Math.ceil(foodDiff)} more kilos of food are needed.`);
    }
}

pets(['2', '10', '1', '1', '1200'])
pets(['5', '10', '2.1', '0.8', '321'])