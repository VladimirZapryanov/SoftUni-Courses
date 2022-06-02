function daysOfWeek(day) {
    let output;

    switch(day) {
        case 'Monday': output = 1; break;
        case 'Tuesday': output = 2; break;
        case 'Wednesday': output = 3; break;
        case 'Thursday': output = 4; break;
        case 'Friday': output = 5; break;
        case 'Saturday': output = 6; break;
        case 'Sunday': output = 7; break;
        default: console.log('error'); break;
    }

    if(output) {
        console.log(output);
    }
}

daysOfWeek('Monday')
daysOfWeek('Friday')
daysOfWeek('Invalid')