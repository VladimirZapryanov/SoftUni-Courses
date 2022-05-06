function hotelRoom(input) {
    let month = input[0];
    let nightCount = Number(input[1]);

    let costForApartment = 0;
    let costForStudio = 0;

    switch(month) {
        case 'May':
        case 'October':
            costForApartment = nightCount * 65;
            costForStudio = nightCount * 50;
            if (nightCount > 7 && nightCount <= 14) {
                costForStudio = costForStudio * 0.95;
            } else if (nightCount > 14) {
                costForStudio = costForStudio * 0.70;
            } break;
            
        case 'June':
        case 'September':
            costForApartment = nightCount * 68.70;
            costForStudio = nightCount * 75.20;
            if (nightCount > 14) {
                costForStudio = costForStudio * 0.80;
            } break;

        case 'July':
        case 'August':
            costForApartment = nightCount * 77;
            costForStudio = nightCount * 76;
            break;
    }

    if (nightCount > 14) {
        costForApartment = costForApartment * 0.90;
    }

    console.log(`Apartment: ${costForApartment.toFixed(2)} lv.`);
    console.log(`Studio: ${costForStudio.toFixed(2)} lv.`);
}

hotelRoom(["May",
"15"])

hotelRoom(["June",
"14"])

hotelRoom(["August",
"20"])

