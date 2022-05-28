function suitcasesLoad(input) {
    let index = 0;
    let luggageCapacity = Number(input[index]);
    index++;
    let command = input[index];
    index++;

    let luggageCount = 1;

    while(command !== 'End') {
        let currentLuggage = Number(command);

        if(luggageCount % 3 === 0) {
            currentLuggage = currentLuggage * 1.1;
            luggageCapacity -= currentLuggage;
        } else {
            luggageCapacity -= currentLuggage;
        }

        if(luggageCapacity >= 0) {
            luggageCount++;
        } else {
            break;
        }

        command = input[index];
        index++;
    }


    if(luggageCapacity >= 0) {
        console.log('Congratulations! All suitcases are loaded!');
    } else {
        console.log('No more space!');
    }

    console.log(`Statistic: ${luggageCount - 1} suitcases loaded.`);
}

suitcasesLoad(["550",
"100",
"252",
"72",
"End"])

suitcasesLoad(["700.5",
"180",
"340.6",
"126",
"220"])

suitcasesLoad(["1200.2",
"260",
"380.5",
"125.6",
"305",
"End"])

