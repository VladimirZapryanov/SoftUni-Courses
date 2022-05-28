function easterBakery(input) {
    let flourPrice = Number(input[0]);
    let flourKilograms = Number(input[1]);
    let sugarKilograms = Number(input[2]);
    let numbersOfEggs = Number(input[3]);
    let packageOfYeast = Number(input[4]);

    let sugarPrice = flourPrice * 0.75;
    let eggsPrice = flourPrice * 1.1;
    let yeastPrice = sugarPrice * 0.2;

    let totalCost = flourKilograms * flourPrice + sugarKilograms * sugarPrice + numbersOfEggs * eggsPrice + packageOfYeast * yeastPrice;
    console.log(totalCost.toFixed(2));
}

easterBakery(["50",
"10",
"3.5",
"6",
"1"])

easterBakery(["63.44",
"3.57",
"6.35",
"8",
"2"])
