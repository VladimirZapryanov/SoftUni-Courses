function fishland(input) {
    let mackerelPricePerKg = Number(input[0]);
    let spratPricePerKg = Number(input[1]);
    let bonitoCount = Number(input[2]);
    let horseMackerelCount = Number(input[3]);
    let musselsCount = Number(input[4]);

    let musselsPricePerKg = 7.50;
    let bonitoPricePricePerKg = mackerelPricePerKg * 1.6;
    let horseMackerelPricePerKg = spratPricePerKg * 1.8;
    let neededMoney = bonitoCount * bonitoPricePricePerKg + horseMackerelCount * horseMackerelPricePerKg + musselsCount * musselsPricePerKg;

    console.log(neededMoney.toFixed(2));
}

fishland(["6.90", "4.20", "1.5", "2.5", "1"])
fishland(["5.55", "3.57", "4.3", "3.6", "7"])