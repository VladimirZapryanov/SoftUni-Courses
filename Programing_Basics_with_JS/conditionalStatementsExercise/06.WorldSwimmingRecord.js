function worldSwimmingRecord(input) {
    let recordInSeconds = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let timeForOneMeters = Number(input[2]);

    let waterResistanceSlows = Math.floor(distanceInMeters / 15) * 12.5;
    let ivanSwimmingTime = distanceInMeters * timeForOneMeters + waterResistanceSlows;
    let neededTime = Math.abs(ivanSwimmingTime - recordInSeconds);
    if (ivanSwimmingTime < recordInSeconds) {
        console.log(`Yes, he succeeded! The new world record is ${ivanSwimmingTime.toFixed(2)} seconds.`);
    } else {
        console.log(`No, he failed! He was ${neededTime.toFixed(2)} seconds slower.`);
    }
}

worldSwimmingRecord(["10464",
"1500",
"20"])

worldSwimmingRecord(["55555.67",
"3017",
"5.03"])
