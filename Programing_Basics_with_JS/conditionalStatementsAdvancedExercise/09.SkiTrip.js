function skiTrip(input) {
    let days = Number(input[0]);
    let kindOfRoom = input[1];
    let rate = input[2];

    let cost = 0;

    switch(kindOfRoom) {
        case 'room for one person':
            cost = (days - 1) * 18.00;
            break;

        case 'apartment':
            cost = (days - 1) * 25.00;
            if (days < 10) {
                cost = cost * 0.7;
            } else if (days >= 10 && days <= 15) {
                cost = cost * 0.65;
            } else {
                cost = cost * 0.50;
            } break;

        case 'president apartment':
            cost = (days - 1) * 35.00;
            if (days < 10) {
                cost = cost * 0.9;
            } else if (days >= 10 && days <= 15) {
                cost = cost * 0.85;
            } else {
                cost = cost * 0.80;
            } break;
    }

    if (rate === 'positive') {
        cost = cost * 1.25;
    } else {
        cost = cost * 0.90;
    }

    console.log(cost.toFixed(2));
}

skiTrip(["14",
"apartment",
"positive"])

skiTrip(["12",
"room for one person",
"positive"])

skiTrip(["2",
"apartment",
"positive"])
