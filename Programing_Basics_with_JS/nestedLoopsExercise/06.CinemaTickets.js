function cinemaTickets(input) {
    let index = 0;
    let command = input[index];
    index++;

    let studentTicketsCount = 0;
    let standardTicketsCount = 0;
    let kidTicketsCount = 0;

    while(command !== 'Finish') {
        let filmName = command;
        let totalFreeSpace = Number(input[index]);
        index++;
        let freeSpaceCounter = totalFreeSpace;
        let secondCommand = input[index];
        index++;
        let occupiedSeats = 0;

        while(secondCommand !== 'End') {
            let kindOfTicket = secondCommand;
            occupiedSeats++;
            freeSpaceCounter--;

            switch(kindOfTicket) {
                case 'student': studentTicketsCount++; break;
                case 'standard': standardTicketsCount++; break;
                case 'kid': kidTicketsCount++; break;
            }

            if(freeSpaceCounter === 0) {
                break;
            }

            secondCommand = input[index];
            index++;
        }

        let occupiedSpacePercent = occupiedSeats / totalFreeSpace * 100;

        console.log(`${filmName} - ${occupiedSpacePercent.toFixed(2)}% full.`);

        command = input[index];
        index++;
    }

    let totalSoldTickets = studentTicketsCount + standardTicketsCount + kidTicketsCount;
    let studentTicketsPercent = studentTicketsCount / totalSoldTickets * 100;
    let standardTicketsPercent = standardTicketsCount / totalSoldTickets * 100;
    let kidTicketsPercent = kidTicketsCount / totalSoldTickets * 100;

    console.log(`Total tickets: ${totalSoldTickets}`);
    console.log(`${studentTicketsPercent.toFixed(2)}% student tickets.`);
    console.log(`${standardTicketsPercent.toFixed(2)}% standard tickets.`);
    console.log(`${kidTicketsPercent.toFixed(2)}% kids tickets.`);
}

cinemaTickets(["Taxi",
"10",
"standard",
"kid",
"student",
"student",
"standard",
"standard",
"End",
"Scary Movie",
"6",
"student",
"student",
"student",
"student",
"student",
"student",
"Finish"])

cinemaTickets(["The Matrix",
"20",
"student",
"standard",
"kid",
"kid",
"student",
"student",
"standard",
"student",
"End",
"The Green Mile",
"17",
"student",
"standard",
"standard",
"student",
"standard",
"student",
"End",
"Amadeus",
"3",
"standard",
"standard",
"standard",
"Finish"])

