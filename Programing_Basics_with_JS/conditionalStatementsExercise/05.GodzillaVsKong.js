function godzillaVsKong(input) {
    let budgetForFilm = Number(input[0]);
    let extrasCount = Number(input[1]);
    let extrasClothesPriceForOne = Number(input[2]);

    let filmSet = budgetForFilm * 0.1;
    let moneyForClothes = extrasCount * extrasClothesPriceForOne;

    if (extrasCount > 150) {
        moneyForClothes = moneyForClothes * 0.9;
    }

    let totalCost = filmSet + moneyForClothes;
    let diffMoney = Math.abs(totalCost - budgetForFilm);

    if (totalCost > budgetForFilm) {
        console.log("Not enough money!");
        console.log(`Wingard needs ${diffMoney.toFixed(2)} leva more.`);
    }   else {
        console.log("Action!");
        console.log(`Wingard starts filming with ${diffMoney.toFixed(2)} leva left.`);
    }
}

godzillaVsKong((["20000",
"120",
"55.5"])
)

godzillaVsKong(["15437.62",
"186",
"57.99"])


godzillaVsKong(["9587.88",
"222",
"55.68"])
