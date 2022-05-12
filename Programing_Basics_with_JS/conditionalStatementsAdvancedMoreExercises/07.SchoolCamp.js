function schoolCamp(input) {
    let season = input[0];
    let typeOfGroup = input[1];
    let numbersOfStudents = Number(input[2]);
    let numbersOfNight = Number(input[3]);

    let pricePerNight = 0;
    let sport = '';

    switch(season) {
        case 'Winter':
            switch(typeOfGroup){
                case 'boys':
                    pricePerNight = 9.60;
                    sport = 'Judo';
                    break;
                case 'girls':
                    pricePerNight = 9.60;
                    sport = 'Gymnastics';
                    break;
                case 'mixed':
                    pricePerNight = 10;
                    sport = 'Ski';
                    break;
            } break;
        case 'Spring':
            switch(typeOfGroup){
                case 'boys':
                    pricePerNight = 7.20;
                    sport = 'Tennis';
                    break;
                case 'girls':
                    pricePerNight = 7.20;
                    sport = 'Athletics';
                    break;
                case 'mixed':
                    pricePerNight = 9.50;
                    sport = 'Cycling';
                    break;
            } break;
        case 'Summer':
            switch(typeOfGroup){
                case 'boys':
                    pricePerNight = 15;
                    sport = 'Football';
                    break;
                case 'girls':
                    pricePerNight = 15;
                    sport = 'Volleyball';
                    break;
                case 'mixed':
                    pricePerNight = 20;
                    sport = 'Swimming';
                    break;
            } break;
    }

    let allNeededMoney = pricePerNight * numbersOfNight * numbersOfStudents;

    if (numbersOfStudents >= 10 && numbersOfStudents < 20) {
        allNeededMoney = allNeededMoney * 0.95;
    } else if (numbersOfStudents >= 20 && numbersOfStudents < 50) {
        allNeededMoney = allNeededMoney * 0.85;
    } else if (numbersOfStudents >= 50) {
        allNeededMoney = allNeededMoney * 0.5;
    }

    console.log(`${sport} ${allNeededMoney.toFixed(2)} lv.`);
}

schoolCamp(['Spring', 'girls', '20', '7'])
schoolCamp(['Winter', 'mixed', '9', '15'])
schoolCamp(['Summer', 'boys', '60', '7'])
schoolCamp(['Spring', 'mixed', '17', '14'])