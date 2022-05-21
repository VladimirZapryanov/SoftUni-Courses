function cake(input) {
    let index = 0;
    let cakeWidth = Number(input[index]);
    index++;
    let cakeLenght = Number(input[index]);
    index++;

    let totalPiecesCake = cakeWidth * cakeLenght;
    let command = input[index];
    index++;

    while(command !== 'STOP'){
        let currentPiecesCake = Number(command);
        totalPiecesCake -= currentPiecesCake;

        if (totalPiecesCake < 0) {
            break;
        }

        command = input[index];
        index++;
    }

    if (totalPiecesCake >= 0) {
        console.log(`${totalPiecesCake} pieces are left.`);
    } else {
        console.log(`No more cake left! You need ${Math.abs(totalPiecesCake)} pieces more.`);
    }
}

cake(["10",
"10",
"20",
"20",
"20",
"20",
"21"])

cake(["10",
"2",
"2",
"4",
"6",
"STOP"])

