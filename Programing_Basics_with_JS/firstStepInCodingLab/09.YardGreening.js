function yardGreening(input) {

    let priceForOneMeter = 7.61;

    let totalMeter = Number(input[0]);

    let totalPrice = priceForOneMeter * totalMeter;
    let discount = totalPrice * 0.18;
    let totalPriceWithDiscount = totalPrice - discount;

    console.log(`The final price is: ${totalPriceWithDiscount} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}

yardGreening(["550"])
yardGreening(["150"])
