function journey(input) {
    let budget = Number(input[0]);
    let season = input[1];

    let totalCost = 0;
    let destination = '';
    let placeToStay = '';
    
    switch(season) {
        case 'summer':
            if (budget <= 100) {
                totalCost = budget * 0.3;
                destination = 'Bulgaria';
                placeToStay = 'Camp';
            } else if (budget <= 1000) {
                totalCost = budget * 0.4;
                destination = 'Balkans';
                placeToStay = 'Camp';
            } else if (budget > 1000) {
                totalCost = budget * 0.9;
                destination = 'Europe';
                placeToStay = 'Hotel';
            } break;

        case 'winter':
            if (budget <= 100) {
                totalCost = budget * 0.7;
                destination = 'Bulgaria';
                placeToStay = 'Hotel';
            } else if (budget <= 1000) {
                totalCost = budget * 0.8;
                destination = 'Balkans';
                placeToStay = 'Hotel';
            } else if (budget > 1000) {
                totalCost = budget * 0.9;
                destination = 'Europe';
                placeToStay = 'Hotel';
            } break;
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${placeToStay} - ${totalCost.toFixed(2)}`);
}

journey(["50", "summer"])
journey(["75", "winter"])
journey(["312", "summer"])
journey(["678.53", "winter"])
journey(["1500", "summer"])