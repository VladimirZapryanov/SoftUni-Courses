function foodDelivery (input) {
    let chikenMenuPrice = 10.35;
    let fishMenuPrice = 12.40;
    let vegMenuPrice = 8.15;
    let delivery = 2.50;

    let chikenMenuCount = Number(input[0]);
    let fishMenuCount = Number(input[1]);
    let vegMenuCount = Number(input[2]);

    let menusCost = chikenMenuCount * chikenMenuPrice + fishMenuCount * fishMenuPrice + vegMenuCount * vegMenuPrice;
    let desertPrice = menusCost * 0.2;
    let totalNeededMoney = menusCost + desertPrice + delivery;

    console.log(totalNeededMoney);
}

foodDelivery(["2", "4", "3"])
foodDelivery(["9", "2", "6"])
