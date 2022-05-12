function sleepyTomCat(input) {
    let holidays = Number(input[0]);

    let tomNormGameMinutes = 30000;
    let allDays = 365;

    let workingDays = allDays - holidays;
    let playingMinutes = workingDays * 63 + holidays * 127;

    let timeDiff = Math.abs(tomNormGameMinutes - playingMinutes);
    let hours = Math.floor(timeDiff / 60);
    let minutes = timeDiff % 60;


    if (tomNormGameMinutes > playingMinutes) {
        console.log('Tom sleeps well');
        console.log(`${hours} hours and ${minutes} minutes less for play`);
    } else {
        console.log('Tom will run away');
        console.log(`${hours} hours and ${minutes} minutes more for play`);
    }
}

sleepyTomCat(['20'])
sleepyTomCat(['113'])