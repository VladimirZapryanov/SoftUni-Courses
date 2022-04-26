function basketballEquipment(input) {
    let yearTrainingFee = Number(input[0]);

    let basketballSneakersPrice = yearTrainingFee - yearTrainingFee * 0.4;
    let basketballClothesPrice = basketballSneakersPrice - basketballSneakersPrice * 0.2;
    let basketballBallPrice = basketballClothesPrice * 0.25;
    let basketballAccessoriesPrice = basketballBallPrice * 0.2;

    let totalMoneyForTraining = yearTrainingFee + basketballSneakersPrice + basketballClothesPrice + basketballBallPrice + basketballAccessoriesPrice;

    console.log(totalMoneyForTraining);
}

basketballEquipment(["365"])
basketballEquipment(["550"])