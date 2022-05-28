function changeBureau(input) {
    let numbersOfBitcoins = Number(input[0]);
    let numbersOfChineseYuan = Number(input[1]);
    let bureauCommission = Number(input[2]);
    
    let bitcoinsBgnPrice = 1168;
    let chineseYuanUsdPrice = 0.15;
    let dolarBgnPrice = 1.76;
    let euroBgnPrice = 1.95;

    let allBitcoinsBgn = numbersOfBitcoins * bitcoinsBgnPrice;
    let allChineseYuanUsd = numbersOfChineseYuan * chineseYuanUsdPrice;
    let allChineseYuanBgn = allChineseYuanUsd * dolarBgnPrice;
    let allMoneyBgn = allBitcoinsBgn + allChineseYuanBgn
    let allMoneyEuro = allMoneyBgn / euroBgnPrice;
    let commission = allMoneyEuro * bureauCommission / 100;
    let moneyAfterCommission = allMoneyEuro - commission;

    console.log(moneyAfterCommission.toFixed(2));
}

changeBureau(['1', '5', '5'])
changeBureau(['20', '5678', '2.4'])