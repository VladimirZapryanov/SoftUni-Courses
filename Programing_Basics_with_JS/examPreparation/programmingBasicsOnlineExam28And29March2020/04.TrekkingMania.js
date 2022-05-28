function trekkingMania(input) {
    let index = 0;
    let groupsCount = Number(input[index]);
    index++;

    let allPeople = 0;
    let groupToMusala = 0;
    let groupToMontBlanc = 0;
    let groupToKilimanjaro = 0;
    let groupToK2 = 0;
    let groupToEverest = 0;

    for(let i = 1; i <= groupsCount; i++){
        let peopleInGroup = Number(input[index]);
        index++;
        allPeople += peopleInGroup;

        if(peopleInGroup <= 5) {
            groupToMusala += peopleInGroup;
        } else if (peopleInGroup <= 12) {
            groupToMontBlanc += peopleInGroup;
        } else if (peopleInGroup <= 25) {
            groupToKilimanjaro += peopleInGroup;
        } else if (peopleInGroup <= 40) {
            groupToK2 += peopleInGroup;
        } else {
            groupToEverest += peopleInGroup;
        }
    }

    let groupToMusalaPercent = groupToMusala / allPeople * 100;
    let groupToMontBlancPercent = groupToMontBlanc / allPeople * 100;
    let groupToKilimanjaroPercent = groupToKilimanjaro / allPeople * 100;
    let groupToK2Percent = groupToK2 / allPeople * 100;
    let groupToEverestPercent = groupToEverest / allPeople * 100;

    console.log(`${groupToMusalaPercent.toFixed(2)}%`);
    console.log(`${groupToMontBlancPercent.toFixed(2)}%`);
    console.log(`${groupToKilimanjaroPercent.toFixed(2)}%`);
    console.log(`${groupToK2Percent.toFixed(2)}%`);
    console.log(`${groupToEverestPercent.toFixed(2)}%`);
}

trekkingMania(["10",
"10",
"5",
"1",
"100",
"12",
"26",
"17",
"37",
"40",
"78"])
