function depositCalculator(input) {
    let depositAmount = Number(input[0]);
    let termOfDeposit = Number(input[1]);
    let annualInterestRate = Number(input[2]);

    let monthInterest = depositAmount * (annualInterestRate / 100) / 12;
    let totalMoney = depositAmount + termOfDeposit * monthInterest;

    console.log(totalMoney);
}

depositCalculator(["200", "3", "5.7"])
depositCalculator(["2350", "6", "7"])