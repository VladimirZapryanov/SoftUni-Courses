function reportSystem(input) {
    let index = 0;
    let searchedMoney = Number(input[index]);
    index++;
    let command = input[index];
    index++;
    let payCount = 0;
    let productBuyWithCard = 0;
    let priceForProductBuyWithCard = 0;
    let productBuyWithCash = 0;
    let priceForProductBuyWithCash = 0;

    while(command !== 'End') {
        payCount++;
        let productPrice = Number(command);

        if(payCount % 2 === 0) {
            if(productPrice < 10) {
                console.log('Error in transaction!');
            } else {
                productBuyWithCard++;
                priceForProductBuyWithCard += productPrice;
                searchedMoney -= productPrice;
                console.log('Product sold!');
            }
        } else {
            if(productPrice > 100) {
                console.log('Error in transaction!');
            } else {
                productBuyWithCash++;
                priceForProductBuyWithCash += productPrice;
                searchedMoney -= productPrice;
                console.log('Product sold!');
            }
        }

        if(searchedMoney <= 0) {
            break;
        }

        command = input[index];
        index++;
    }

    let averagePaymentsWithCard = priceForProductBuyWithCard / productBuyWithCard;
    let averagePaymentsWithCash = priceForProductBuyWithCash / productBuyWithCash;

    if(searchedMoney <= 0) {
        console.log(`Average CS: ${averagePaymentsWithCash.toFixed(2)}`);
        console.log(`Average CC: ${averagePaymentsWithCard.toFixed(2)}`);
    } else {
        console.log('Failed to collect required money for charity.');
    }
}

reportSystem(['500', '120', '8', '63', '256', '78', '317'])
reportSystem(['600', '86', '150', '98', '227', 'End'])