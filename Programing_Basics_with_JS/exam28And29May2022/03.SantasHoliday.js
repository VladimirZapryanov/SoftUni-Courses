function santasHoliday(input) {
    let days = Number(input[0]);
    let kindOfRoom = input[1];
    let grade = input[2];
    
    let nightCost = 0;
    let roomPrice = 18
    let apartmentPrice = 25;
    let presidentApartmentPrice = 35;
    let night = days - 1;

    switch(kindOfRoom) {
        case 'room for one person': nightCost = night * roomPrice; break;
        case 'apartment': 
        nightCost = night * apartmentPrice; 
            if(days < 10) {
                nightCost = nightCost * 0.70;
            } else if (days <= 15) {
                nightCost = nightCost * 0.65;
            } else {
                nightCost = nightCost * 0.50;
            }
        break;

        case 'president apartment': 
        nightCost = night * presidentApartmentPrice; 
        if(days < 10) {
            nightCost = nightCost * 0.90;
        } else if (days <= 15) {
            nightCost = nightCost * 0.85;
        } else {
            nightCost = nightCost * 0.80;
        }
        break; 
    }

    let totalCost = 0;

    if(grade === 'positive') {
        totalCost = nightCost * 1.25;
    } else if (grade === 'negative') {
        totalCost = nightCost * 0.9;
    }

    console.log(totalCost.toFixed(2));
}

santasHoliday(["14",
"apartment",
"positive"])

santasHoliday(["30",
"president apartment",
"negative"])

santasHoliday(["12",
"room for one person",
"positive"])

santasHoliday(["2",
"apartment",
"positive"])


