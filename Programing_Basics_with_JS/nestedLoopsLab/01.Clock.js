function clock() {

    for(let hours = 0; hours <= 23; hours++) {
        for(let minutes = 0; minutes <= 59; minutes++) {
            console.log(`${hours}:${minutes}`);
        }
    }
}

clock()