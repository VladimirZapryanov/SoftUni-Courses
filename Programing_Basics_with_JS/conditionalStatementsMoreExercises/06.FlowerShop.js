function flowerShop(input) {
    let numberOfMagnolias = Number(input[0]);
    let numberOfHyacinths = Number(input[1]);
    let numberOfRoses = Number(input[2]);
    let numberOfCacti = Number(input[3]);
    let giftPrice = Number(input[4]);

    let magnoliaPrice = 3.25;
    let hyacinthPrice = 4.00;
    let rosePrice = 3.50;
    let cactusPrice = 8.00;

    let totalProfit = numberOfMagnolias * magnoliaPrice + numberOfHyacinths * hyacinthPrice + numberOfRoses * rosePrice + numberOfCacti * cactusPrice;
    let profitWithoutTaxes = totalProfit * 0.95;

    let moneyDiff = Math.abs(giftPrice - profitWithoutTaxes);

    if (profitWithoutTaxes >= giftPrice) {
        console.log(`She is left with ${Math.floor(moneyDiff)} leva.`);
    } else {
        console.log(`She will have to borrow ${Math.ceil(moneyDiff)} leva.`);
    }
}

flowerShop(['2', '3', '5', '1', '50'])
flowerShop(['15', '7', '5', '10', '100'])