function building(input) {
    let numbersOfFloor = Number(input[0]);
    let numbersOfRooms = Number(input[1]);

    for(let f = numbersOfFloor; f >= 1 ; f--) {
        let result = '';

        for(let r = 0; r < numbersOfRooms; r++){

            if(f === numbersOfFloor) {
                result += `L${f}${r} `;
            } else if (f % 2 === 1) {
                result += `A${f}${r} `;
            } else if (f % 2 == 0) {
                result += `O${f}${r} `;
            }
        }

        console.log(result);
    }
}

building(['6', '4'])
building(['9', '5'])
building(['4', '4'])