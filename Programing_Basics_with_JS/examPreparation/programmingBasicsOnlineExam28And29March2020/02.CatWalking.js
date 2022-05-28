function catWalking(input) {
    let minutesWalking = Number(input[0]);
    let numbersOfWalking = Number(input[1]);
    let caloriesPerDay = Number(input[2]);

    let burnCaloriesPerMinutes = 5;
    let allBurnCalories = (minutesWalking * numbersOfWalking) * burnCaloriesPerMinutes; 
    let neededBurnCalories = caloriesPerDay / 2;

    if(allBurnCalories >= neededBurnCalories) {
        console.log(`Yes, the walk for your cat is enough. Burned calories per day: ${allBurnCalories}.`);
    } else {
        console.log(`No, the walk for your cat is not enough. Burned calories per day: ${allBurnCalories}.`);
    }
}

catWalking(["30",
"3",
"600"])

catWalking(["15",
"2",
"500"])

catWalking(["40",
"2",
"300"])
