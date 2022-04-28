function lunchBreak(input) {
    let nameOfMovie = input[0];
    let episodeDuration = Number(input[1]);
    let breakDuration = Number(input[2]);

    let lunchTime = breakDuration / 8;
    let restTime = breakDuration / 4;
    let freeTime = breakDuration - (lunchTime + restTime);
    let finalBreakMinutes = freeTime - episodeDuration;
    let neededTime = Math.abs(finalBreakMinutes);

    if (freeTime >= episodeDuration) {
        console.log(`You have enough time to watch ${nameOfMovie} and left with ${Math.ceil(finalBreakMinutes)} minutes free time.`);
    } else {
        console.log(`You don't have enough time to watch ${nameOfMovie}, you need ${Math.ceil(neededTime)} more minutes.`);
    }
}

lunchBreak(["Game of Thrones",
"60",
"96"])

lunchBreak(["Teen Wolf",
"48",
"60"])
