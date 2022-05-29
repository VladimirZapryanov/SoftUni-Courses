function easterEggs(input) {
    let index = 0;
    let eggsCount = Number(input[index]);
    index++

    let redEggs = 0;
    let orangeEggs = 0;
    let blueEggs = 0;
    let greenEggs = 0;

    for(let i = 1; i <= eggsCount; i ++) {
        let eggColour = input[index];
        index++;

        switch(eggColour) {
            case 'red': redEggs++; break;
            case 'orange': orangeEggs++; break;
            case 'blue': blueEggs++; break;
            case 'green': greenEggs++; break;
        }
    }

    let maxEggs = Math.max(redEggs, orangeEggs, blueEggs, greenEggs);
    let colourOfMaxEggs = '';
    if(maxEggs === redEggs) {
        colourOfMaxEggs = 'red';
    } else if (maxEggs === orangeEggs){
        colourOfMaxEggs = 'orange';
    } else if (maxEggs === blueEggs) {
        colourOfMaxEggs = 'blue';
    } else {
        colourOfMaxEggs = 'green';
    }

    console.log(`Red eggs: ${redEggs}`);
    console.log(`Orange eggs: ${orangeEggs}`);
    console.log(`Blue eggs: ${blueEggs}`);
    console.log(`Green eggs: ${greenEggs}`);
    console.log(`Max eggs: ${maxEggs} -> ${colourOfMaxEggs}`);
}

easterEggs(["7",
"orange",
"blue",
"green",
"green",
"blue",
"red",
"green"])

easterEggs(["4",
"blue",
"red",
"blue",
"orange"]) 

