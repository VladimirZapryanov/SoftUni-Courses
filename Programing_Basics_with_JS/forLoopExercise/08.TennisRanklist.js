function tennisRanklist(input) {
    let index = 0;
    let tournamentsCount = Number(input[index]);
    index++;
    let ranklistStartPoints = Number(input[index]);
    index++;

    let ranklistPoints = 0;
    let totalWins = 0;

    for (let i = 1; i <= tournamentsCount; i++) {
        let tournamentReachedStage = input[index];
        index++;

        switch(tournamentReachedStage) {
            case 'W':
                ranklistPoints += 2000;
                totalWins ++;
                break;
            case 'F':
                ranklistPoints += 1200;
                break;
            case 'SF':
                ranklistPoints += 720;
                break;
        }
    }

    let finalPoints = ranklistStartPoints + ranklistPoints;
    let averagePoints = Math.floor(ranklistPoints / tournamentsCount);
    let winsPercent = totalWins / tournamentsCount * 100;

    console.log(`Final points: ${finalPoints}`);
    console.log(`Average points: ${averagePoints}`);
    console.log(`${winsPercent.toFixed(2)}%`);
}

tennisRanklist(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"])

tennisRanklist(["4",
"750",
"SF",
"W",
"SF",
"W"])

