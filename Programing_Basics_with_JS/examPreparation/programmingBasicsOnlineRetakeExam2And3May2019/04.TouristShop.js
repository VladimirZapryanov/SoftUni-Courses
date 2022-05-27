function touristShop(input) {
    let index = 0;
    let budget = Number(input[index]);
    index++;
    let command = input[index];
    index++;

    let productCount = 0;
    let totalCost = 0;

    while(command !== 'Stop') {
        let productName = command;
        let productPrice = Number(input[index]);
        index++;
        productCount++;

        if(productCount % 3 === 0) {
            productPrice = productPrice * 0.5;
            totalCost += productPrice;
        } else {
            totalCost += productPrice;
        }

        if(totalCost > budget) {
            break;
        }

        command = input[index];
        index++
    }

    let moneyDiff = Math.abs(budget - totalCost);

    if(budget >= totalCost) {
        console.log(`You bought ${productCount} products for ${totalCost.toFixed(2)} leva.`);
    } else {
        console.log("You don't have enough money!");
        console.log(`You need ${moneyDiff.toFixed(2)} leva!`);
    }
}

touristShop(["153.20",
"Backpack",
"25.20",
"Shoes",
"54",
"Sunglasses",
"30",
"Stop"])

touristShop(["54",
"Thermal underwear",
"24",
"Sunscreen",
"45"])
