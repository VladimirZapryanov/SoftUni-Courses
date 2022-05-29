function footballKit(input) {
    let tshirtPrice = Number(input[0]);
    let moneyTillToWinBall = Number(input[1]);

    let pantsPrice = tshirtPrice * 0.75;
    let socksPrice = pantsPrice * 0.2;
    let shoosesPrice = (pantsPrice + tshirtPrice) * 2;
    let cost = tshirtPrice + pantsPrice + socksPrice + shoosesPrice;
    let totalCost = cost * 0.85;

    let neededMoney = moneyTillToWinBall - totalCost;

    if(totalCost >= moneyTillToWinBall) {
        console.log('Yes, he will earn the world-cup replica ball!');
        console.log(`His sum is ${totalCost.toFixed(2)} lv.`);
    } else {
        console.log('No, he will not earn the world-cup replica ball.');
        console.log(`He needs ${neededMoney.toFixed(2)} lv. more.`);
    }
}

footballKit(["25",
"100"])

footballKit(["55",
"310"])

footballKit(["59.99",
"500"])
