function balls(input) {
    let index = 0;
    let numbersOfBalls = Number(input[index]);
    index++;

    let redBallPoints = 5;
    let orangeBallPoints = 10;
    let yellowBallPoints = 15;
    let whiteBallPoints = 20;
    let blackBallPoints = 0.5;

    let redBallCount = 0;
    let orangeBallCount = 0;
    let yellowBallCount = 0;
    let whiteBallCount = 0;
    let blackBallCount = 0;
    let otherBallCount = 0;
    let totalPoints = 0;


    for(let i = 1; i <= numbersOfBalls; i++) {
        let kindOfBall = input[index];
        index++;

        switch(kindOfBall) {
            case 'red':
                redBallCount++;
                totalPoints += redBallPoints;
                break;

            case 'orange':
                orangeBallCount++;
                totalPoints += orangeBallPoints;
                break;

            case 'yellow':
                yellowBallCount++;
                totalPoints += yellowBallPoints;
                break;

            case 'white':
                whiteBallCount++;
                totalPoints += whiteBallPoints;
                break;

            case 'black':
                blackBallCount++;
                totalPoints = Math.floor(totalPoints * blackBallPoints);
                break;

            default: 
                otherBallCount++;
                break;
        }
    }

    console.log(`Total points: ${totalPoints}`);
    console.log(`Red balls: ${redBallCount}`);
    console.log(`Orange balls: ${orangeBallCount}`);
    console.log(`Yellow balls: ${yellowBallCount}`);
    console.log(`White balls: ${whiteBallCount}`);
    console.log(`Other colors picked: ${otherBallCount}`);
    console.log(`Divides from black balls: ${blackBallCount}`);
}

balls(["3",
"white",
"black",
"pink"])

balls(["5",
"red",
"red",
"ddd",
"ddd",
"ddd"])

balls(['10',
    'white',
    'white',
    'ee',
    'red',
    'orange',
    'red',
    'black',
    'black',
    'black',
    'black'])
