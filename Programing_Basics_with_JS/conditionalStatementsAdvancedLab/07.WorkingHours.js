function workingHours(input) {
    let hours = Number(input[0]);
    let day = input[1];

    let openHour = 10;
    let closeHour = 18;
    let openOrClose = 'closed'
    
    if (day === 'Monday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    } else if (day === 'Tuesday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    } else if (day === 'Wednesday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    } else if (day === 'Thursday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    } else if (day === 'Friday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    } else if (day === 'Saturday' && openHour <= hours && hours <= closeHour) {
        openOrClose = 'open';
    }
    console.log(openOrClose);
}

workingHours(['11', 'Monday'])
workingHours(['19', 'Friday'])
workingHours(['11', 'Sunday'])