function cinemaTickets(input) {
    let index = 0;
    let command = input[index];
    index++;

    let totalStudentTickets = 0;
    let totalStandardTickets = 0;
    let totalKidsTickets = 0;

    while(command !== 'Finish') {
        let movieName = command;
        let roomFreeSpace = Number(input[index]);
        index++;
        let occupancyCount = 0;
        newCommand = input[index];
        index++;

        while(newCommand !== 'End') {
            let kindOfTickets = newCommand;
            occupancyCount++;
            
            switch(kindOfTickets) {
                case 'student': totalStudentTickets++; break;
                case 'standard': totalStandardTickets++; break;
                case 'kid': totalKidsTickets++; break;
            }

            if (roomFreeSpace === occupancyCount) {
                break;
            }

            newCommand = input[index];
            index++;
        }

        let roomOccupancyPercent = occupancyCount / roomFreeSpace * 100;
        console.log(`${movieName} - ${roomOccupancyPercent.toFixed(2)}% full.`);

        command = input[index];
        index++;
    }

    let allTickets = totalStudentTickets + totalStandardTickets + totalKidsTickets;
    let studentTicketsPercent = totalStudentTickets / allTickets * 100;
    let standardTicketsPercent = totalStandardTickets / allTickets * 100;
    let kidTicketsPercent = totalKidsTickets / allTickets * 100;

    console.log(`Total tickets: ${allTickets}`);
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