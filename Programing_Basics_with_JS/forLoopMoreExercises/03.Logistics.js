function logistics(input) {
    let index = 0;
    let numbersOfCargo = Number(input[index]);
    index++;

    let minibusPrice = 200;
    let truckPrice = 175;
    let trainPrice = 120;

    let minibusTons = 0;
    let truckTons = 0;
    let trainTons = 0;

    let totalMoney = 0;
    let allTons = 0;

    for (let i = 1; i <= numbersOfCargo; i++) {
        let tonsOfCargo = Number(input[index]);
        index++;

        if (tonsOfCargo <= 3) {
            minibusTons += tonsOfCargo;
            totalMoney += tonsOfCargo * minibusPrice;
            allTons += tonsOfCargo;
        } else if (tonsOfCargo <= 11) {
            truckTons += tonsOfCargo;
            totalMoney += tonsOfCargo * truckPrice;
            allTons += tonsOfCargo;
        } else {
            trainTons += tonsOfCargo;
            totalMoney += tonsOfCargo * trainPrice;
            allTons += tonsOfCargo;
        }
    }

    let averagePrice = totalMoney / allTons;

    let minibusTonsPercent = minibusTons / allTons * 100;
    let truckTonsPercent = truckTons / allTons * 100;
    let trainTonsPercent = trainTons / allTons * 100;
    console.log(averagePrice.toFixed(2));
    console.log(`${minibusTonsPercent.toFixed(2)}%`);
    console.log(`${truckTonsPercent.toFixed(2)}%`);
    console.log(`${trainTonsPercent.toFixed(2)}%`);
}

logistics(['4', '1', '5', '16', '3'])
logistics(['5', '2', '10', '20', '1', '7'])