function cinemaVoucher(input) {
    let index = 0;
    let voucherValue = Number(input[index]);
    index++;
    command = input[index];
    index++;

    let ticketsCount = 0;
    let productCount = 0;

    while(command !== 'End') {
        let productType = command;
        let currentProductPrice = 0;
        if(productType.length > 8) {
            let firstSymbol = productType.charCodeAt([0]);
            let secondSymbol = productType.charCodeAt([1]);
            currentProductPrice = firstSymbol + secondSymbol;

            if (currentProductPrice <= voucherValue) {
                ticketsCount++;
                voucherValue -= currentProductPrice;
            } else {
                break;
            }
        } else {
            currentProductPrice = productType.charCodeAt([0]);
            if (currentProductPrice <= voucherValue) {
                productCount++;
                voucherValue -= currentProductPrice;
            } else {
                break;
            }
        }

        command = input[index];
        index++;
    }

    console.log(ticketsCount);
    console.log(productCount);
}

cinemaVoucher(["300",
"Captain Marvel",
"popcorn",
"Pepsi"])

cinemaVoucher(["1500",
"Avengers: Endgame",
"Bohemian Rhapsody",
"Deadpool 2",
"End"])
