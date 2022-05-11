function cleverLily(input) {
    let lilyAge = Number(input[0]);
    let washingMachinePrice = Number(input[1]);
    let toyPrice = Number(input[2]);

    let toysCount = 0;
    let lilysGiftMoney = 0;
    let lilysMoney = 0;
    let brothersMoney = 0;

    for (let i = 1; i <= lilyAge; i++) {
        if (i % 2 === 0) {
            lilysGiftMoney += 10;
            lilysMoney += lilysGiftMoney;
            brothersMoney++;
        } else {
            toysCount++;
        }
    }

    lilysMoney += (toysCount * toyPrice) - brothersMoney;

    let moneyDiff = Math.abs(lilysMoney - washingMachinePrice);

    if (lilysMoney >= washingMachinePrice) {
        console.log(`Yes! ${moneyDiff.toFixed(2)}`);
    } else {
        console.log(`No! ${moneyDiff.toFixed(2)}`);
    }
}

cleverLily(["10",
"170.00",
"6"])

cleverLily(["21",
"1570.98",
"3"])
