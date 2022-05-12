function truckDriver(input) {
    let season = input[0];
    let kilometersPerMonth = Number(input[1]);

    let totalKilometers = kilometersPerMonth * 4;
    let money = 0;

    if (kilometersPerMonth <= 5000) {
        switch(season) {
            case 'Summer': money = totalKilometers * 0.90; break;
            case 'Winter': money = totalKilometers * 1.05; break;
            case 'Spring':
            case 'Autumn': money = totalKilometers * 0.75; break;
        }
    } else if (kilometersPerMonth <= 10000) {
        switch(season) {
            case 'Summer': money = totalKilometers * 1.10; break;
            case 'Winter': money = totalKilometers * 1.25; break;
            case 'Spring':
            case 'Autumn': money = totalKilometers * 0.95; break;
        }
    } else if (kilometersPerMonth <= 20000) {
        switch(season) {
            case 'Summer': 
            case 'Winter': 
            case 'Spring':
            case 'Autumn': money = totalKilometers * 1.45; break;
        }
    }

    let finalMoney = money * 0.90;

    console.log(finalMoney.toFixed(2));
}

truckDriver(['Summer', '3455'])
truckDriver(['Winter', '4350'])
truckDriver(['Spring', '1600'])
truckDriver(['Winter', '5678'])
truckDriver(['Autumn', '8600'])
truckDriver(['Winter', '16042'])
truckDriver(['Spring', '16942'])