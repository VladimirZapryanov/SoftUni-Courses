function tradeCommissions(input) {
    let city = input[0];
    let sales = Number(input[1]);

    let commissions = 0;

    switch(city) {
        case 'Sofia':
            if (0 <= sales && sales <= 500) {
                commissions = sales * 5 / 100;
            } else if (500 < sales && sales <= 1000) {
                commissions = sales * 7 / 100;
            } else if (1000 < sales && sales <= 10000) {
                commissions = sales * 8 / 100;
            } else if (10000 < sales) {
                commissions = sales * 12 / 100;
            } else console.log('error')
            break;
        case 'Varna':
            if (0 <= sales && sales <= 500) {
                commissions = sales * 4.5 / 100;
            } else if (500 < sales && sales <= 1000) {
                commissions = sales * 7.5 / 100;
            } else if (1000 < sales && sales <= 10000) {
                commissions = sales * 10 / 100;
            } else if (10000 < sales) {
                commissions = sales * 13 / 100;
            } else console.log('error')
            break;
        case 'Plovdiv':
            if (0 <= sales && sales <= 500) {
                commissions = sales * 5.5 / 100;
            } else if (500 < sales && sales <= 1000) {
                commissions = sales * 8 / 100;
            } else if (1000 < sales && sales <= 10000) {
                commissions = sales * 12 / 100;
            } else if (10000 < sales) {
                commissions = sales * 14.5 / 100;
            } else console.log('error')
            break;
        default: console.log('error')
    }

    if (commissions > 0) {
        console.log(commissions.toFixed(2));
    }  
}

tradeCommissions(['Sofia', '300'])
tradeCommissions(['Plovdiv', '499.99'])
tradeCommissions(['Varna', '3874.50'])
tradeCommissions(['Kaspichan', '300'])
tradeCommissions(['Sofia', -'50'])
