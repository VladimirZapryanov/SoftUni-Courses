function easterParty(input) {
    let guest = Number(input[0]);
    let priceForOnePerson = Number(input[1]);
    let budget = Number(input[2]);
    
    let cakePrice = budget * 0.10;

    if(guest >= 10 && guest <= 15) {
        priceForOnePerson = priceForOnePerson * 0.85;
    } else if (guest > 15 && guest <= 20) {
        priceForOnePerson = priceForOnePerson * 0.80;
    } else if (guest > 20) {
        priceForOnePerson = priceForOnePerson * 0.75;
    }

    let allEnvelopesPrice = guest * priceForOnePerson;
    let totalCost = allEnvelopesPrice + cakePrice;  
    let moneyDiff = Math.abs(budget - totalCost);

    if(budget >= totalCost) {
        console.log(`It is party time! ${moneyDiff.toFixed(2)} leva left.`);
    } else {
        console.log(`No party! ${moneyDiff.toFixed(2)} leva needed.`);
    }
}

easterParty(["18",
"30",
"450"])

easterParty(["8",
"25",
"340"])

easterParty(["24",
"35",
"550"])
