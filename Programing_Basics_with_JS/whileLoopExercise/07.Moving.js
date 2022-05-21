function moving(input) {
    let index = 0;
    let widthFreeSpace = Number(input[index]);
    index++;
    let lengthFreeSpace = Number(input[index]);
    index++;
    let heightFreeSpace = Number(input[index]);
    index++;

    let totalFreeSpace = widthFreeSpace * lengthFreeSpace * heightFreeSpace;
    let command = input[index];
    index++;

    while(command !== 'Done') {
        let currentLuggage = Number(command);
        totalFreeSpace -= currentLuggage;

        if (totalFreeSpace < 0) {
            break;
        }

        command = input[index];
        index++;
    }

    if (totalFreeSpace >= 0) {
        console.log(`${totalFreeSpace} Cubic meters left.`);
    } else {
        console.log(`No more free space! You need ${Math.abs(totalFreeSpace)} Cubic meters more.`);

    }
}

moving(["10", 
"10",
"2",
"20",
"20",
"20",
"20",
"122"])

moving(["10", 
"1",
"2",
"4", 
"6",
"Done"])
