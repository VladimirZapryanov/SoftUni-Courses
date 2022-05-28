function foodForPets(input) {
    let index = 0;
    let days = Number(input[index]);
    index++;
    let allFood = Number(input[index]);
    index++

    let dogFood = 0;
    let catFood = 0;
    let eatenBiscuits = 0;

    for(let i = 1; i <= days; i++) {
        let currentDogFood = Number(input[index]);
        index++;
        let currentCatFood = Number(input[index]);
        index++;

        dogFood += currentDogFood;
        catFood += currentCatFood;

        let dayFoot = currentDogFood + currentCatFood;

        if(i % 3 === 0) {
            eatenBiscuits += dayFoot * 0.1;
        }
    }

    let allEatenFood = dogFood + catFood;
    let dogFoodPercent = dogFood / allEatenFood * 100;
    let catFoodPercent = catFood / allEatenFood * 100;
    let allEatenFoodPercent = allEatenFood / allFood * 100;
    
    console.log(`Total eaten biscuits: ${Math.floor(eatenBiscuits)}gr.`);
    console.log(`${allEatenFoodPercent.toFixed(2)}% of the food has been eaten.`);
    console.log(`${dogFoodPercent.toFixed(2)}% eaten from the dog.`);
    console.log(`${catFoodPercent.toFixed(2)}% eaten from the cat.`);
}

foodForPets(["3",
"1000",
"300",
"20",
"100",
"30",
"110",
"40"])

foodForPets(["3",
"500",
"100",
"30",
"110",
"25",
"120",
"35"])

