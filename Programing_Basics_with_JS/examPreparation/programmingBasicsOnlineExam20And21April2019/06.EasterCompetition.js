function easterCompetition(input) {
    let index = 0;
    let easterCakeCount = Number(input[index]);
    index++;

    let topScore = Number.MIN_SAFE_INTEGER;
    let topBaker = ''

    for(let i = 1; i <= easterCakeCount; i++) {
        let bakerName = input[index];
        index++;
        let command = input[index];
        index++;

        let bakerScore = 0;

        while(command !== 'Stop') {
            let score = Number(command);
            bakerScore += score;


            command = input[index];
            index++;
        }

        console.log(`${bakerName} has ${bakerScore} points.`);
        if(bakerScore > topScore) {
            topScore = bakerScore;
            topBaker = bakerName;
            console.log(`${bakerName} is the new number 1!`);
        }
    }

    console.log(`${topBaker} won competition with ${topScore} points!`);
}

easterCompetition(["3",
"Chef Manchev", "10",
"10",
"10",
"10",
"Stop",
"Natalie",
"8",
"2",
"9",
"Stop",
"George",
"9",
"2",
"4",
"2",
"Stop"])

easterCompetition(["2",
"Chef Angelov",
"9",
"9",
"9",
"Stop",
"Chef Rowe",
"10",
"10",
"10",
"10",
"Stop"])

