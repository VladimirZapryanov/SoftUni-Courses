function minNumber(input) {
    let index = 0;
    data = input[index];
    index++;

    let minNumber = Number.MAX_SAFE_INTEGER;


    while(data !== 'Stop') {
        let number = Number(data);

        if (number < minNumber) {
            minNumber = number;
        }

        data = input[index];
        index++;
    }
    
    console.log(minNumber);
}

minNumber(["100",
"99",
"80",
"70",
"Stop"])

minNumber(["-10",
"20",
"-30",
"Stop"])

minNumber(["45",
"-20",
"7",
"99",
"Stop"])

minNumber(["999",
"Stop"])

minNumber(["-1",
"-2",
"Stop"])
