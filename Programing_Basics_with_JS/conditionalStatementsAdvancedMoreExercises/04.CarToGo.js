function carToGo(input) {
    let budget = Number(input[0]);
    let season = input[1];

    let classType = '';
    let carType = '';
    let carPrice = 0;

    if (budget <= 100) {
        classType = 'Economy class';
        if (season === 'Summer') {
            carType = 'Cabrio';
            carPrice = budget * 0.35;
        } else {
            carType = 'Jeep';
            carPrice = budget * 0.65;
        }
    } else if (budget <= 500) {
        classType = 'Compact class';
        if (season === 'Summer') {
            carType = 'Cabrio';
            carPrice = budget * 0.45;
        } else {
            carType = 'Jeep';
            carPrice = budget * 0.80;
        }
    } else {
        classType = 'Luxury class';
        carType = 'Jeep';
        carPrice = budget * 0.9;
    }

    console.log(`${classType}`);
    console.log(`${carType} - ${carPrice.toFixed(2)}`);
}

carToGo(['450', 'Summer'])
carToGo(['450', 'Winter'])
carToGo(['1010', 'Summer'])
carToGo(['1010', 'Winter'])
carToGo(['99.99', 'Summer'])
carToGo(['70.50', 'Winter'])