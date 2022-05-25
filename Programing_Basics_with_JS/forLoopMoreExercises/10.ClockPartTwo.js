function clock() {
    for(let hours = 0; hours <= 23; hours++) {
        for(let minutes = 0; minutes <= 59; minutes++) {
            for(let seconds = 0; seconds <= 59; seconds++) {
                console.log(`${hours} : ${minutes} : ${seconds}`);
            }
        }
    }
}

clock()