function aluminumJoinery(input) {
    let numbersOfJoinery = Number(input[0]);
    let kindOfJoinery = input[1];
    let delivery = input[2];

    let joineryCost = 0;
    let deliveryPrice = 60;

    switch(kindOfJoinery) {
        case '90X130': 
        joineryCost += numbersOfJoinery * 110;
        if (numbersOfJoinery > 60) {
            joineryCost -= joineryCost * 0.08;
        } else if (numbersOfJoinery > 30) {
            joineryCost -= joineryCost * 0.05;
        }; break;

        case '100X150': 
        joineryCost += numbersOfJoinery * 140;
        if (numbersOfJoinery > 80) {
            joineryCost -= joineryCost * 0.1;
        } else if (numbersOfJoinery > 40) {
            joineryCost -= joineryCost * 0.06;
        }; break;

        case '130X180': 
        joineryCost += numbersOfJoinery * 190;
        if (numbersOfJoinery > 50) {
            joineryCost -= joineryCost * 0.12;
        } else if (numbersOfJoinery > 20) {
            joineryCost -= joineryCost * 0.07;
        }; break;

        case '200X300': 
        joineryCost += numbersOfJoinery * 250;
        if (numbersOfJoinery > 50) {
            joineryCost -= joineryCost * 0.14;
        } else if (numbersOfJoinery > 25) {
            joineryCost -= joineryCost * 0.09;
        }; break;
    }

    if(delivery === 'With delivery') {
        joineryCost += deliveryPrice;
    }

    if(numbersOfJoinery > 99) {
        joineryCost -= joineryCost * 0.04;
    }

    if(numbersOfJoinery < 10) {
        console.log('Invalid order');
    } else {
        console.log(`${joineryCost.toFixed(2)} BGN`);
    }
}

aluminumJoinery(["40", 
"90X130",
"Without delivery"])

aluminumJoinery(["105",
"100X150",
"With delivery"])

aluminumJoinery(["2",
"130X180",
"With delivery"])
