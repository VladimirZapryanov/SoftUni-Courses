function godzillaVsKong(input) {
    let filmBudget = Number(input[0]);
    let numberForExtras = Number(input[1]);
    let clothingPriceForOne = Number(input[2]);

    let decorPrice = filmBudget * 0.10;
    let clothingPriceForAll = numberForExtras * clothingPriceForOne;

    if(numberForExtras > 150) {
        clothingPriceForAll = clothingPriceForAll * 0.90;
    }

    let totalNeededMoney = clothingPriceForAll + decorPrice;

    let moneyDiff = Math.abs(filmBudget - totalNeededMoney);

    if(filmBudget < totalNeededMoney) {
        console.log('Not enough money!');
        console.log(`Wingard needs ${moneyDiff.toFixed(2)} leva more.`);
    } else {
        console.log('Action!');
        console.log(`Wingard starts filming with ${moneyDiff.toFixed(2)} leva left.`);
    }
}

godzillaVsKong(["20000", 
"120",
"55.5"])

godzillaVsKong(["15437.62",
"186",
"57.99"])

godzillaVsKong(["9587.88",
"222",
"55.68"])

