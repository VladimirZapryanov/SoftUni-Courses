function oscarsWeekInCinema(input) {
    let filmName = input[0];
    let typeOfRoom = input[1];
    let ticketsCount = Number(input[2]);

    let totalProfit = 0;
    
    switch(filmName) {
        case 'A Star Is Born':
            switch(typeOfRoom) {
                case 'normal': totalProfit = ticketsCount * 7.50; break;
                case 'luxury': totalProfit = ticketsCount * 10.50; break;
                case 'ultra luxury': totalProfit = ticketsCount * 13.50; break;
            } break;
        
        case 'Bohemian Rhapsody':
            switch(typeOfRoom) {
                case 'normal': totalProfit = ticketsCount * 7.35; break;
                case 'luxury': totalProfit = ticketsCount * 9.45; break;
                case 'ultra luxury': totalProfit = ticketsCount * 12.75; break;
            } break;

        case 'Green Book':
            switch(typeOfRoom) {
                case 'normal': totalProfit = ticketsCount * 8.15; break;
                case 'luxury': totalProfit = ticketsCount * 10.25; break;
                case 'ultra luxury': totalProfit = ticketsCount * 13.25; break;
            } break;
        
        case 'The Favourite':
            switch(typeOfRoom) {
                case 'normal': totalProfit = ticketsCount * 8.75; break;
                case 'luxury': totalProfit = ticketsCount * 11.55; break;
                case 'ultra luxury': totalProfit = ticketsCount * 13.95; break;
            } break;
    }

    console.log(`${filmName} -> ${totalProfit.toFixed(2)} lv.`);
}   

oscarsWeekInCinema(["A Star Is Born",
"luxury",
"42"])

oscarsWeekInCinema(["Green Book",
"normal",
"63"])
