function trekkingMania(input) {
    let index = 0;
    let numbersOfGroups = Number(input[index]);
    index++;

    let musala = 0;
    let montBlanc = 0;
    let kilimanjaro = 0;
    let k2 = 0;
    let everest = 0;
    let totalPeople = 0;


    for (let i = 1; i <= numbersOfGroups; i ++) {
        let peopleInEachGroup = Number(input[index]);
        index++;

        if (peopleInEachGroup <= 5) {
            musala += peopleInEachGroup;
            totalPeople += peopleInEachGroup;
        } else if (peopleInEachGroup <= 12) {
            montBlanc += peopleInEachGroup;
            totalPeople += peopleInEachGroup;
        } else if (peopleInEachGroup <= 25) {
            kilimanjaro += peopleInEachGroup;
            totalPeople += peopleInEachGroup;
        } else if (peopleInEachGroup <= 40) {
            k2 += peopleInEachGroup;
            totalPeople += peopleInEachGroup;
        } else {
            everest += peopleInEachGroup;
            totalPeople += peopleInEachGroup;
        }
    }

    let musalaPercent = musala / totalPeople * 100;
    let montBlancPercent = montBlanc / totalPeople * 100;
    let kilimanjaroPercent = kilimanjaro / totalPeople * 100;
    let k2Percent = k2 / totalPeople * 100;
    let everestPercent = everest / totalPeople * 100;

    console.log(`${musalaPercent.toFixed(2)}%`);
    console.log(`${montBlancPercent.toFixed(2)}%`);
    console.log(`${kilimanjaroPercent.toFixed(2)}%`);
    console.log(`${k2Percent.toFixed(2)}%`);
    console.log(`${everestPercent.toFixed(2)}%`);
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

trekkingMania(["5",
"25",
"41",
"31",
"250",
"6"])


