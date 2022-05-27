function oscarsCeremony(input) {
    let roomRent = Number(input[0]);

    let statuettesPrice = roomRent * 0.7;
    let cateringPrice = statuettesPrice * 0.85;
    let soundSystemPrice = cateringPrice * 0.5;

    let totalCost = roomRent + statuettesPrice + cateringPrice + soundSystemPrice;

    console.log(totalCost.toFixed(2));
}

oscarsCeremony(['3500'])
oscarsCeremony(['5555'])