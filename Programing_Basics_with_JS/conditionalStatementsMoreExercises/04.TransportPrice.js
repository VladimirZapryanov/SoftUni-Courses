function transportPrice(input) {
    let kilometers = Number(input[0]);
    let dayPeriod = input[1];

    let price = 0;

    if (kilometers < 20) {
        price += 0.70;
        if (dayPeriod === 'day') {
            price += kilometers * 0.79;
        } else if (dayPeriod === 'night') {
            price += kilometers * 0.90;
        }
    } else if (kilometers < 100) {
        price = kilometers * 0.09;
    } else {
        price = kilometers * 0.06;
    }
    
    console.log(price.toFixed(2));
}

transportPrice(['5', 'day'])
transportPrice(['7', 'night'])
transportPrice(['25', 'day'])
transportPrice(['180', 'night'])