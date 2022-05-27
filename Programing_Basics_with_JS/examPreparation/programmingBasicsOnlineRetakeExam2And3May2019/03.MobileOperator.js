function mobileOperation(input) {
    let periodOfContract = input[0];
    let typeOfContract = input[1];
    let mobileInternet = input[2];
    let numbersOfMonth = Number(input[3]);

    let pricePerMonth = 0;

    switch(periodOfContract) {
        case 'one':
            switch(typeOfContract) {
                case 'Small': pricePerMonth = 9.98; break;
                case 'Middle': pricePerMonth = 18.99; break;
                case 'Large': pricePerMonth = 25.98; break;
                case 'ExtraLarge': pricePerMonth = 35.99; break;
            } break;

        case 'two':
            switch(typeOfContract) {
                case 'Small': pricePerMonth = 8.58; break;
                case 'Middle': pricePerMonth = 17.09; break;
                case 'Large': pricePerMonth = 23.59; break;
                case 'ExtraLarge': pricePerMonth = 31.79; break;
            } break;
    }

    if(mobileInternet === 'yes') {
        if(pricePerMonth <= 10) {
            pricePerMonth += 5.50;
        } else if (pricePerMonth <= 30) {
            pricePerMonth += 4.35;
        } else if (pricePerMonth > 30) {
            pricePerMonth += 3.85;
        }
    }

    let totalCost = pricePerMonth * numbersOfMonth;

    if(periodOfContract === 'two') {
        totalCost = totalCost * 0.9625;
    }

    console.log(`${totalCost.toFixed(2)} lv.`);
}

mobileOperation(["one",
"Small",
"yes",
"10"])

mobileOperation(["two",
"Large",
"no",
"10"])
