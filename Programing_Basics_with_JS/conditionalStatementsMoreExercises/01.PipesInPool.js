function pipesInPool(input) {
    let poolVolume = Number(input[0]);
    let firstPipeFlowRate = Number(input[1]);
    let secondPipeFlowRate = Number(input[2]);
    let hoursWithoutWorker = Number(input[3]);

    let firstPipeLiters = firstPipeFlowRate * hoursWithoutWorker;
    let secondPipeLiters = secondPipeFlowRate * hoursWithoutWorker;
    let poolWater = firstPipeLiters + secondPipeLiters;
    let poolWaterPercent = poolWater / poolVolume * 100;
    let firstPipeLitersPercent = firstPipeLiters / poolWater * 100;
    let secondPipeLitersPercent = secondPipeLiters / poolWater * 100;
    let overFlowsLiters = poolWater - poolVolume;

    if (poolWater <= poolVolume) {
        console.log(`The pool is ${poolWaterPercent.toFixed(2)}% full. Pipe 1: ${firstPipeLitersPercent.toFixed(2)}%. Pipe 2: ${secondPipeLitersPercent.toFixed(2)}%.`);
    } else {
        console.log(`For ${hoursWithoutWorker.toFixed(2)} hours the pool overflows with ${overFlowsLiters.toFixed(2)} liters.`);
    }
}

pipesInPool(['1000', '100', '120', '3'])
pipesInPool(['100', '100', '100', '2.5'])