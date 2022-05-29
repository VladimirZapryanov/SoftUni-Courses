function easterTrip(input) {
    let destination = input[0];
    let date = input[1];
    let nightsCount = Number(input[2]);
    
    let nightsPrice = 0;

    switch(destination) {
        case 'France':
            switch(date) {
                case '21-23': nightsPrice = 30; break;
                case '24-27': nightsPrice = 35; break;
                case '28-31': nightsPrice = 40; break;
            } break;
        
         case 'Italy':
            switch(date) {
                case '21-23': nightsPrice = 28; break;
                case '24-27': nightsPrice = 32; break;
                case '28-31': nightsPrice = 39; break;
            } break;

         case 'Germany':
            switch(date) {
                case '21-23': nightsPrice = 32; break;
                case '24-27': nightsPrice = 37; break;
                case '28-31': nightsPrice = 43; break;
            } break;
    }

    let allCost = nightsCount * nightsPrice;
    console.log(`Easter trip to ${destination} : ${allCost.toFixed(2)} leva.`);
}

easterTrip(["Germany",
"24-27",
"5"])

easterTrip(["Italy",
"21-23",
"7"])

easterTrip(["France",
"28-31",
"8"])
