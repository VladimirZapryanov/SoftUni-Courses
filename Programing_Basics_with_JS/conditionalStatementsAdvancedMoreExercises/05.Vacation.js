function vacation(input) {
    let budget = Number(input[0]);
    let season = input[1];

    let placeToStay = '';
    let location = '';
    let vacationPrice = 0;

    if (budget <= 1000) {
        placeToStay = 'Camp';
        if (season === 'Summer') {
            location = 'Alaska';
            vacationPrice = budget * 0.65;
        } else {
            location = 'Morocco';
            vacationPrice = budget * 0.45;
        }
    } else if (budget <= 3000) {
        placeToStay = 'Hut';
        if (season === 'Summer') {
            location = 'Alaska';
            vacationPrice = budget * 0.80;
        } else {
            location = 'Morocco';
            vacationPrice = budget * 0.60;
        }
    } else {
        placeToStay = 'Hotel';
        vacationPrice = budget * 0.90;
        if (season === 'Summer') {
            location = 'Alaska';
        } else {
            location = 'Morocco';
        }
    }

    console.log(`${location} - ${placeToStay} - ${vacationPrice.toFixed(2)}`);
}

vacation(['800', 'Summer'])
vacation(['799.50', 'Winter'])
vacation(['3460', 'Summer'])
vacation(['1100', 'Summer'])
vacation(['5000', 'Winter'])
vacation(['2543.99', 'Winter'])