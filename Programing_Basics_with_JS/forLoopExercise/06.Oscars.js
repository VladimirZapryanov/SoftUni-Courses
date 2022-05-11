function oscars(input) {
    let index = 0;
    let actorName = input[index];
    index++;
    let actorPoints = Number(input[index]);
    index++;
    let estimatorsNumber = Number(input[index]);
    index++;

    let notNominated = false;

    for (let i = 1; i <= estimatorsNumber; i++){
        let estimatorName = input[index];
        index++;
        let estimatorPoints = Number(input[index]);
        index++;

        actorPoints += (estimatorName.length * estimatorPoints) / 2;

        if (actorPoints > 1250.5) {
            notNominated = true;
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${actorPoints.toFixed(1)}!`);
            break;
        } 
    }

    if (!notNominated) {
        let neededPoints = Math.abs(actorPoints - 1250.5);
        console.log(`Sorry, ${actorName} you need ${neededPoints.toFixed(1)} more!`);
    }
}

oscars(["Zahari Baharov",
"205",
"4",
"Johnny Depp",
"45",
"Will Smith",
"29",
"Jet Lee",
"10",
"Matthew Mcconaughey",
"39"])

oscars(["Sandra Bullock",
"340",
"5",
"Robert De Niro",
"50",
"Julia Roberts",
"40.5",
"Daniel Day-Lewis",
"39.4",
"Nicolas Cage",
"29.9",
"Stoyanka Mutafova",
"33"])
