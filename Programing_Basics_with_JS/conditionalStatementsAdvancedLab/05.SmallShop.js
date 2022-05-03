function smallShop(input) {
    let product = input[0];
    let city = input[1];
    let productQuantity = Number(input[2]);

    let totalPrice = 0;

    if (city === 'Sofia') {
        switch(product) {
            case 'coffee': totalPrice = productQuantity * 0.50; break;
            case 'water': totalPrice = productQuantity * 0.80; break;
            case 'beer': totalPrice = productQuantity * 1.20; break;
            case 'sweets': totalPrice = productQuantity * 1.45; break;
            case 'peanuts': totalPrice = productQuantity * 1.60; break;
        }
    } else if (city === 'Plovdiv') {
        switch(product) {
            case 'coffee': totalPrice = productQuantity * 0.40; break;
            case 'water': totalPrice = productQuantity * 0.70; break;
            case 'beer': totalPrice = productQuantity * 1.15; break;
            case 'sweets': totalPrice = productQuantity * 1.30; break;
            case 'peanuts': totalPrice = productQuantity * 1.50; break;
        }
    } else if (city === 'Varna') {
        switch(product) {
            case 'coffee': totalPrice = productQuantity * 0.45; break;
            case 'water': totalPrice = productQuantity * 0.70; break;
            case 'beer': totalPrice = productQuantity * 1.10; break;
            case 'sweets': totalPrice = productQuantity * 1.35; break;
            case 'peanuts': totalPrice = productQuantity * 1.55; break;
        }
    }
    console.log(totalPrice);
}

smallShop(['coffee', 'Varna', '2'])
smallShop(['peanuts', 'Plovdiv', '1'])
smallShop(['beer', 'Sofia', '2'])
smallShop(['water', 'Plovdiv', '2'])
smallShop(['sweets', 'Sofia', '2.23'])

