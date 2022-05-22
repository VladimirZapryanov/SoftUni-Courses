function traveling(input) {
    let index = 0;
    let command = input[index];
    index++;

    let savedMoney = 0;

    while(command !== 'End') {
        let destination = command;
        let destinationPrice = Number(input[index]);
        index++;

        while(savedMoney < destinationPrice) {
            let money = Number(input[index]);
            index++;
            savedMoney += money;

            if (savedMoney >= destinationPrice) {
                console.log(`Going to ${destination}!`);
                savedMoney = 0;
                break;
            }
        }
    
    command = input[index];
    index++;
    }
}

traveling(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"])

traveling(["France",
"2000",
"300",
"300",
"200",
"400",
"190",
"258",
"360",
"Portugal",
"1450",
"400",
"400",
"200",
"300",
"300",
"Egypt",
"1900",
"1000",
"280",
"300",
"500",
"End"])

