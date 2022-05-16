function maxNumber(input) {
    let index = 0;
    data = input[index];
    index++;

    let maxNumber = Number.MIN_SAFE_INTEGER;


    while(data !== 'Stop') {
        let number = Number(data);

        if (number > maxNumber) {
            maxNumber = number;
        }

        data = input[index];
        index++;
    }
    
    console.log(maxNumber);
}

maxNumber(["100",
"99",
"80",
"70",
"Stop"])

maxNumber(["-10",
"20",
"-30",
"Stop"])

maxNumber(["45",
"-20",
"7",
"99",
"Stop"])

maxNumber(["999",
"Stop"])

maxNumber(["-1",
"-2",
"Stop"])

