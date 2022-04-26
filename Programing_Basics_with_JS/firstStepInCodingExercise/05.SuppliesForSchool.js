function suppliesForSchool (input) {
    let priceOfPenPakage = 5.80;
    let pricePerMarkerPakage = 7.20;
    let priceForDetergent = 1.2;

    let countOfPenPakage = Number(input[0]);
    let countOfMarkerPakage = Number(input[1]);
    let littersOfDetergent = Number(input[2]);
    let discount = Number(input[3]);

    let neededMoneyForPens = countOfPenPakage * priceOfPenPakage;
    let neededMoneyForMarker = countOfMarkerPakage * pricePerMarkerPakage;
    let neededMoneyForDetergent = littersOfDetergent * priceForDetergent;
    let totalNeededMoney = neededMoneyForPens + neededMoneyForMarker + neededMoneyForDetergent;
    let totalNeededMoneyWithDiscount = totalNeededMoney - totalNeededMoney * (discount / 100);

    console.log(totalNeededMoneyWithDiscount);
}

suppliesForSchool(["2", "3", "4", "25"])
suppliesForSchool(["4", "2", "5", "13"])