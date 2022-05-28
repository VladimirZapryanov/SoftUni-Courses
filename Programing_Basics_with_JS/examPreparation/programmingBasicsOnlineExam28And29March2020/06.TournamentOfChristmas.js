function tournamentOfChristmas(input) {
    let index = 0;
    let days = Number(input[index]);
    index++;

    let winMoney = 0;
    let winDays =0;
    let loseDays = 0;

    for(let i = 1; i <= days; i++) {
        let command = input[index];
        index++;    
        
        let currentWinMoney = 0;
        let winGames = 0;
        let loseGames = 0;

        while(command !== 'Finish') {
            let gameResult = input[index];
            index++;

            if(gameResult === 'win') {
                currentWinMoney += 20;
                winGames++;
            } else if (gameResult === 'lose') {
                loseGames++;
            }

            command = input[index];
            index++;
        }

        if(winGames > loseGames) {
            currentWinMoney = currentWinMoney * 1.1;
            winDays++;
        } else {
            loseDays++;
        }

        winMoney += currentWinMoney;

    }

    if(winDays > loseDays) {
        winMoney = winMoney * 1.2;
        console.log(`You won the tournament! Total raised money: ${winMoney.toFixed(2)}`);
    } else {
        console.log(`You lost the tournament! Total raised money: ${winMoney.toFixed(2)}`);
    }
}

tournamentOfChristmas(["2",
"volleyball",
"win",
"football",
"lose",
"basketball",
"win",
"Finish",
"golf",
"win",
"tennis",
"win",
"badminton",
"win",
"Finish"])

tournamentOfChristmas(["3",
"darts",
"lose",
"handball",
"lose",
"judo",
"win",
"Finish",
"snooker",
"lose",
"swimming",
"lose",
"squash",
"lose",
"table tennis",
"win",
"Finish",
"volleyball",
"win",
"basketball",
"win",
"Finish"])
