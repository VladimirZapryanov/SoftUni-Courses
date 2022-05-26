function dishwasher(input) {
    let index = 0;
    let detergentBottles = Number(input[index]);
    index++;

    let volumeOfBottle = 750;
    let potNeededDetergent = 15;
    let plateNeededDetergent = 5;
    let totalDetergent = detergentBottles * volumeOfBottle;
    let dishwasherloadingCount = 0;
    let command = input[index];
    index++;
    let plateCount = 0;
    let potCount = 0;


    while(command !== 'End') {
        let numberOfVessels = Number(command);
        dishwasherloadingCount++;

        if(dishwasherloadingCount % 3 === 0) {
            potCount += numberOfVessels;
            totalDetergent -= numberOfVessels * potNeededDetergent;
        } else {
            plateCount += numberOfVessels;
            totalDetergent -= numberOfVessels * plateNeededDetergent;
        }

        if(totalDetergent < 0) {
            break;
        }

        command = input[index];
        index++;
    }

    if(totalDetergent >= 0) {
        console.log('Detergent was enough!');
        console.log(`${plateCount} dishes and ${potCount} pots were washed.`);
        console.log(`Leftover detergent ${totalDetergent} ml.`);
    } else {
        console.log(`Not enough detergent, ${Math.abs(totalDetergent)} ml. more necessary!`);
    }
}

dishwasher(['2', '53', '65', '55', 'End'])
dishwasher(['1', '10', '15', '10', '12', '13', '30'])