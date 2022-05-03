function fruitShop(input) {
    let product = input[0];
    let day = input[1];
    let productQuantity = Number(input[2]);

    let totalMoney = 0;

    if (day === 'Monday') {
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.50; break;
            case 'apple': totalMoney = productQuantity * 1.20; break;
            case 'orange': totalMoney = productQuantity * 0.85; break;
            case 'grapefruit': totalMoney = productQuantity * 1.45; break;
            case 'kiwi': totalMoney = productQuantity * 2.70; break;
            case 'pineapple': totalMoney = productQuantity * 5.50; break;
            case 'grapes': totalMoney = productQuantity * 3.85; break;
            default: console.log('error'); break;
        } 
    } else if (day === 'Tuesday'){
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.50; break;
            case 'apple': totalMoney = productQuantity * 1.20; break;
            case 'orange': totalMoney = productQuantity * 0.85; break;
            case 'grapefruit': totalMoney = productQuantity * 1.45; break;
            case 'kiwi': totalMoney = productQuantity * 2.70; break;
            case 'pineapple': totalMoney = productQuantity * 5.50; break;
            case 'grapes': totalMoney = productQuantity * 3.85; break;
            default: console.log('error'); break;
        }
    } else if (day === 'Wednesday') {
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.50; break;
            case 'apple': totalMoney = productQuantity * 1.20; break;
            case 'orange': totalMoney = productQuantity * 0.85; break;
            case 'grapefruit': totalMoney = productQuantity * 1.45; break;
            case 'kiwi': totalMoney = productQuantity * 2.70; break;
            case 'pineapple': totalMoney = productQuantity * 5.50; break;
            case 'grapes': totalMoney = productQuantity * 3.85; break;
            default: console.log('error'); break;
        } 
    } else if (day === 'Thursday') {
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.50; break;
            case 'apple': totalMoney = productQuantity * 1.20; break;
            case 'orange': totalMoney = productQuantity * 0.85; break;
            case 'grapefruit': totalMoney = productQuantity * 1.45; break;
            case 'kiwi': totalMoney = productQuantity * 2.70; break;
            case 'pineapple': totalMoney = productQuantity * 5.50; break;
            case 'grapes': totalMoney = productQuantity * 3.85; break;
            default: console.log('error'); break;
        }
    } else if (day === 'Friday'){
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.50; break;
            case 'apple': totalMoney = productQuantity * 1.20; break;
            case 'orange': totalMoney = productQuantity * 0.85; break;
            case 'grapefruit': totalMoney = productQuantity * 1.45; break;
            case 'kiwi': totalMoney = productQuantity * 2.70; break;
            case 'pineapple': totalMoney = productQuantity * 5.50; break;
            case 'grapes': totalMoney = productQuantity * 3.85; break;
            default: console.log('error'); break;
        }
    }  else if (day === 'Saturday'){
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.70; break;
            case 'apple': totalMoney = productQuantity * 1.25; break;
            case 'orange': totalMoney = productQuantity * 0.90; break;
            case 'grapefruit': totalMoney = productQuantity * 1.60; break;
            case 'kiwi': totalMoney = productQuantity * 3.00; break;
            case 'pineapple': totalMoney = productQuantity * 5.60; break;
            case 'grapes': totalMoney = productQuantity * 4.20; break;
            default: console.log('error'); break;
        }
    } else if (day === 'Sunday'){
        switch(product) {
            case 'banana': totalMoney = productQuantity * 2.70; break;
            case 'apple': totalMoney = productQuantity * 1.25; break;
            case 'orange': totalMoney = productQuantity * 0.90; break;
            case 'grapefruit': totalMoney = productQuantity * 1.60; break;
            case 'kiwi': totalMoney = productQuantity * 3.00; break;
            case 'pineapple': totalMoney = productQuantity * 5.60; break;
            case 'grapes': totalMoney = productQuantity * 4.20; break;
            default: console.log('error'); break;
        }
    } else {
        console.log('error');
    }

    if (totalMoney > 0) {
        console.log(`${totalMoney.toFixed(2)}`);
    }
}

fruitShop(["apple",
"Tuesday",
"2"])

fruitShop(["orange",
"Sunday",
"3"])

fruitShop(["kiwi",
"Monday",
"2.5"])

fruitShop(["grapes",
"Saturday",
"0.5"])

fruitShop(["tomato",
"Monday",
"0.5"])
