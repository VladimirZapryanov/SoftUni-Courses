function bestPlayer(input) {
    let index = 0;
    let command = input[index];
    index++;

    let bestPlayerName = '';
    let bestPlayerScore = 0;
    let hetrick = false;

    while(command !== 'END') {
        let playerName = command;
        let playerScore = Number(input[index]);
        index++;

        if(playerScore > bestPlayerScore) {
            bestPlayerScore = playerScore;
            bestPlayerName = playerName;
        }
        
        if(playerScore >= 10) {
            hetrick = true;
            break;
        } else if (playerScore >= 3) {
            hetrick = true;
        }

        command = input[index];
        index++;
    }

    console.log(`${bestPlayerName} is the best player!`);

    if(hetrick) {
        console.log(`He has scored ${bestPlayerScore} goals and made a hat-trick !!!`);
    } else {
        console.log(`He has scored ${bestPlayerScore} goals.`);
    }
}

bestPlayer(["Neymar", "2",
"Ronaldo",
"1",
"Messi",
"3",
"END"])

bestPlayer(["Silva",
"5",
"Harry Kane",
"10"])

bestPlayer(["Petrov",
"2",
"Drogba",
"11"])
