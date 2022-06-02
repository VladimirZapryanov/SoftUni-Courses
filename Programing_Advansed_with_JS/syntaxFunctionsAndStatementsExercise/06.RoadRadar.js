function roadRadar(speed, area) {
    let speedLimit = 0;
    let status = '';

    switch (area) {
        case 'motorway': speedLimit = 130; break;
        case 'interstate': speedLimit = 90; break;
        case 'city': speedLimit = 50; break;
        case 'residential': speedLimit = 20; break;
    }

    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    } else {
        let speedDiff = speed - speedLimit;

        if (speedDiff <= 20) {
            status = 'speeding';
        } else if (speedDiff <= 40) {
            status = 'excessive speeding';
        } else {
            status = 'reckless driving';
        }

        console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
}

roadRadar(40, 'city')
roadRadar(21, 'residential')
roadRadar(120, 'interstate')
roadRadar(200, 'motorway')