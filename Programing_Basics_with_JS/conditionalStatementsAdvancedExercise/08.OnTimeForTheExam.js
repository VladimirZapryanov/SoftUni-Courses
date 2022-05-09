function onTimeForTheExam(input) {
    let examHours = Number(input[0]);
    let examMinutes = Number(input[1]);
    let arrivalHours = Number(input[2]);
    let arrivalMinutes = Number(input[3]);

    let examTime = examHours * 60 + examMinutes;
    let arrivalTime = arrivalHours * 60 + arrivalMinutes;
    let timeDiff = examTime - arrivalTime;
    let timeDiffHour = Math.trunc(timeDiff / 60);
    let timeDiffMinutes = Math.abs(timeDiff) % 60;

    if (arrivalTime > examTime) {
        console.log('Late');

        if (Math.abs(timeDiff) <= 59) {
            console.log(`${Math.abs(timeDiff)} minutes after the start`);
        } else if (Math.abs(timeDiff) >= 60 && timeDiffMinutes < 10) {
            console.log(`${Math.abs(timeDiffHour)}:0${timeDiffMinutes} hours after the start`);
        }   else {
            console.log(`${Math.abs(timeDiffHour)}:${timeDiffMinutes} hours after the start`);
        }

    } else if (timeDiff === 0 || timeDiff <= 30) {
        console.log('On time');
        if (timeDiff !== 0) {
            console.log(`${timeDiff} minutes before the start`);
        }

    } else if (timeDiff > 30) {
        console.log('Early');

        if (timeDiff <= 59) {
            console.log(`${timeDiff} minutes before the start`);
        } else if (timeDiff >= 60 && timeDiffMinutes < 10) {
            console.log(`${timeDiffHour}:0${timeDiffMinutes} hours before the start`);
        } else {
            console.log(`${timeDiffHour}:${timeDiffMinutes} hours before the start`);
        }
    }
}

onTimeForTheExam(["9",
"30",
"9",
"50"])

onTimeForTheExam(["9",
"00",
"8",
"30"])

onTimeForTheExam(["16",
"00",
"15",
"00"])

onTimeForTheExam(["9",
"00",
"10",
"30"])

onTimeForTheExam(["14",
"00",
"13",
"55"])

onTimeForTheExam(["11",
"30",
"8",
"12"])

onTimeForTheExam(["10",
"00",
"10",
"00"])

onTimeForTheExam(["11",
"30",
"10",
"55"])

onTimeForTheExam(["11",
"30",
"12",
"29"])

