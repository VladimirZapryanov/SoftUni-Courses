function fruit(fruitName, weightInGrams, pricePerKilogram) {
    let weightInKilograms = weightInGrams / 1000;
    let neededMoney = weightInKilograms * pricePerKilogram;

    console.log(`I need $${neededMoney.toFixed(2)} to buy ${weightInKilograms.toFixed(2)} kilograms ${fruitName}.`);
}

fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)