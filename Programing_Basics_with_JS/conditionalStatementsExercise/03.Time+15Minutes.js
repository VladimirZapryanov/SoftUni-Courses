function time(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1]);
    
    let totalMinutes = hours * 60 + minutes + 15;
    let calcHours = Math.floor(totalMinutes / 60);
    let calcMinutes = totalMinutes % 60;

    if (calcHours > 23) {
        calcHours -= 24;
    }

    if (calcMinutes < 10) {
        console.log(`${calcHours}:0${calcMinutes}`);
    } else {
        console.log(`${calcHours}:${calcMinutes}`);
    }
}

time(["1", "46"])
time(["0", "01"])
time(["23", "59"])
time(["11", "08"])
time(["12", "49"])