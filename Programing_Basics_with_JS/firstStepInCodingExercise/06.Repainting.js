function repainting(input) {
    let nylonPrice = 1.50;
    let paintPrice = 14.50;
    let paintThinnerPrice = 5.00;
    let bagsPrice = 0.40;
    let extraNylon = 2;
    let workerPrice = 0.3;

    let nylonAmount = Number(input[0]);
    let paintAmount = Number(input[1]);
    let thinnerAmount = Number(input[2]);
    let workingHours = Number(input[3]);

    let extraPaint = paintAmount * 0.1;

    let totalNylonAmount = nylonAmount + extraNylon;
    let totalPaintAmount = paintAmount + extraPaint;
    let neededMoneyForMaterials = totalNylonAmount * nylonPrice +  totalPaintAmount * paintPrice + thinnerAmount * paintThinnerPrice + bagsPrice;
    let workersPriceForOneHour = neededMoneyForMaterials * workerPrice;
    let totalWorkerPrice = workersPriceForOneHour * workingHours;
    let totalNeededMoney = neededMoneyForMaterials + totalWorkerPrice;

    console.log(totalNeededMoney);
}

repainting(["10", "11", "4", "8"])
repainting(["5", "10", "10", "1"])