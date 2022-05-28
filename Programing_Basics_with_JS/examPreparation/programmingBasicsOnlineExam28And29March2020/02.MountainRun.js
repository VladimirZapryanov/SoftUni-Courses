function mountainRun(input) {
    let record = Number(input[0]);
    let distance = Number(input[1]);
    let timeForOneMeter = Number(input[2]);

    let slowsItDown = Math.floor(distance / 50) * 30;
    let newTime = (distance * timeForOneMeter) + slowsItDown;
    let timeDiff = newTime - record;

    if(newTime < record) {
        console.log(`Yes! The new record is ${newTime.toFixed(2)} seconds.`);
    } else {
        console.log(`No! He was ${timeDiff.toFixed(2)} seconds slower.`);
    }
}

mountainRun(["10164",
"1400",
"25"])

mountainRun(["5554.36",
"1340",
"3.23"])

mountainRun(["1377",
"389",
"3"])
