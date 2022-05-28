function careOfPuppy(input) {
    let index = 0;
    let kilogramsOfFood = Number(input[index]);
    index++;
    let command = input[index];
    index++;

    let gramesOfFood = kilogramsOfFood * 1000;

    while(command !== 'Adopted') {
        let currentEatenFood = command;
        gramesOfFood -= currentEatenFood;

        command = input[index];
        index++;
    }

    if(gramesOfFood >= 0) {
        console.log(`Food is enough! Leftovers: ${gramesOfFood} grams.`);
    } else {
        console.log(`Food is not enough. You need ${Math.abs(gramesOfFood)} grams more.`);
    }
}

careOfPuppy(["4",
"130",
"345",
"400",
"180",
"230",
"120",
"Adopted"])

careOfPuppy(["3",
"1000",
"1000",
"1000",
"Adopted"])

careOfPuppy(["2",
"999",
"456",
"999",
"999",
"123",
"456",
"Adopted"])
