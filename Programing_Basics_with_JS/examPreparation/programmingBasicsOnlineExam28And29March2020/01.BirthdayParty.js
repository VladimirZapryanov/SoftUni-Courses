function birthdayParty(arg) {
    let roomRent = Number(arg);

    let cakePrice = roomRent * 0.2;
    let drinksPrice = cakePrice * 0.55;
    let animatorPrice = roomRent / 3;

    let neededMoney = roomRent + cakePrice + drinksPrice + animatorPrice;

    console.log(neededMoney);
}

birthdayParty(['2250'])
birthdayParty(['3720'])