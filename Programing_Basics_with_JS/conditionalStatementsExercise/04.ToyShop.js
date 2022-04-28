function toyShop(input) {
    let puzzlePrice = 2.60;
    let talkingDollPrice = 3;
    let teddyBearPrice = 4.10;
    let minionPrice = 8.20;
    let truckPrice = 2;

    let tripPrice = Number(input[0]);
    let puzzleCount = Number(input[1]);
    let talkingDollCount = Number(input[2]);
    let teddyBearCount = Number(input[3]);
    let minionCount = Number(input[4]);
    let truckCount = Number(input[5]);

    let orderPrice = puzzlePrice * puzzleCount + talkingDollPrice * talkingDollCount + teddyBearPrice * teddyBearCount + minionPrice * minionCount + truckPrice * truckCount;
    let orderCount = puzzleCount + talkingDollCount + teddyBearCount + minionCount + truckCount;

    if (orderCount >= 50) {
        orderPrice = orderPrice * 0.75;
    }

    orderPrice = orderPrice * 0.9;
    finalMoney = orderPrice - tripPrice;

    if (finalMoney >= 0) {
        console.log(`Yes! ${finalMoney.toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${Math.abs(finalMoney).toFixed(2)} lv needed.`);
    }
}

toyShop(["40.8",
"20",
"25",
"30",
"50",
"10"])

toyShop(["320",
"8",
"2",
"5",
"5",
"1"])
