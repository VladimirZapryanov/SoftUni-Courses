function walking(input) {
    let index = 0;
    let targetSteps = 10000;
    let command = input[index];
    index++;

    let steps = 0;

    while(command !== 'Going home') {
        steps += Number(command);

        if (steps >= targetSteps) {
            break;
        }

        command = input[index];
        index++;
    }

    if (command === 'Going home') {
        steps += Number(input[index]);
    }

    let stepsDiff = Math.abs(targetSteps - steps);

    if (steps >= targetSteps) {
        console.log('Goal reached! Good job!');
        console.log(`${stepsDiff} steps over the goal!`);
    } else {
        console.log(`${stepsDiff} more steps to reach goal.`);
    }
}

walking(["1000",
"1500",
"2000",
"6500"])

walking(["1500",
"300",
"2500",
"3000",
"Going home",
"200"])

walking(["1500",
"3000",
"250",
"1548",
"2000",
"Going home",
"2000"])

walking(["125",
"250",
"4000",
"30",
"2678",
"4682"])
