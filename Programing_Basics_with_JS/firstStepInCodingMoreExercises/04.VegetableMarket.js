function vegetableMarket(input) {
    let vegetabslePricePerKg = Number(input[0]);
    let fruitsPricePerKg = Number(input[1]);
    let allKgVegetables = Number(input[2]);
    let allKgFruits = Number(input[3]);

    let totalProfitInBgn = vegetabslePricePerKg * allKgVegetables + fruitsPricePerKg * allKgFruits;
    let totalProfitInEuro = totalProfitInBgn / 1.94;

    console.log(totalProfitInEuro.toFixed(2));
}

vegetableMarket(["0.194", "19.4", "10", "10"])
vegetableMarket(["1.5", "2.5", "10", "10"])