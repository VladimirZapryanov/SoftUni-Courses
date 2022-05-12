function harvest(input) {
    let vineyard = Number(input[0]);
    let grapesPerMeter = Number(input[1]);
    let neededWineLiters = Number(input[2]);
    let numberOfWorkers = Number(input[3]);

    let wineVineyard = vineyard * 0.4;
    let allGrapes = grapesPerMeter * wineVineyard;
    let litersWine = allGrapes / 2.5;

    let wineDiff = Math.abs(neededWineLiters - litersWine);
    let wineForOneWorker = wineDiff / numberOfWorkers;

    if (neededWineLiters > litersWine) {
        console.log(`It will be a tough winter! More ${Math.floor(wineDiff)} liters wine needed.`);
    } else {
        console.log(`Good harvest this year! Total wine: ${Math.floor(litersWine)} liters.`);
        console.log(`${Math.ceil(wineDiff)} liters left -> ${Math.ceil(wineForOneWorker)} liters per person.`);
    }
}

harvest(['650', '2', '175', '3'])
harvest(['1020', '1.5', '425', '4'])