function vatParking(input) {
    let numbersOfDays = Number(input[0]);
    let numbersOfHours = Number(input[1]);

    let totalCostAllDays = 0;

    for(let day = 1; day <= numbersOfDays; day++) {
        let currentCost = 0;
        for(let hour = 1; hour <= numbersOfHours; hour++) {
            let cost = 0;
            if(day % 2 === 0 && hour % 2 === 1) {
                currentCost += 2.50;
                cost += 2.5;
            } else if (day % 2 === 1 && hour % 2 === 0) {
                currentCost += 1.25;
                cost += 1.25;
            } else {
                currentCost++;
                cost++;
            }

            totalCostAllDays += cost;
            if(hour === numbersOfHours) {
                console.log(`Day: ${day} - ${currentCost.toFixed(2)} leva`);
            }
        }
    }

    console.log(`Total: ${totalCostAllDays.toFixed(2)} leva`);
}

vatParking(["2",
"5"])
