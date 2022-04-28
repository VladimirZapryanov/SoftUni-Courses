function shopping(input) {
    let budgetOfPetur = Number(input[0]);
    let videoCardCount = Number(input[1]);
    let processorCount = Number(input[2]);
    let memoryCount = Number(input[3]);

    let videoCardPrice = 250;
    let allVideoCardPrice = videoCardCount * videoCardPrice;
    let processorPrice = allVideoCardPrice * 0.35;
    let allProcessorPrice = processorCount * processorPrice;
    let memoryPrice = allVideoCardPrice * 0.1;
    let allMemoryPrice = memoryCount * memoryPrice;
    let neededMoney = allVideoCardPrice + allProcessorPrice + allMemoryPrice;

    if (videoCardCount > processorCount) {
        neededMoney = neededMoney * 0.85;
    }

    let diffMoney = budgetOfPetur - neededMoney;

    if (diffMoney >= 0) {
        console.log(`You have ${diffMoney.toFixed(2)} leva left!`);
    } else {
        console.log(`Not enough money! You need ${Math.abs(diffMoney).toFixed(2)} leva more!`);
    }
}

shopping(["900",
"2",
"1",
"3"])

shopping(["920.45",
"3",
"1",
"1"])


