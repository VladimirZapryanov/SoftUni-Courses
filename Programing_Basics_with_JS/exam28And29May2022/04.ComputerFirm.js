function computerFirm(input) {
    let index = 0;
    let computerCount = Number(input[index]);
    index++

    let totalRaiting = 0;
    let totalSales = 0;

    for(let i = 1; i <= computerCount; i++) {
        let computerModel = input[index];
        index++
        let computerRaiting = computerModel[2];
        totalRaiting += Number(computerRaiting);
        let possibleSales = Number(computerModel[0] + computerModel[1]);

        switch(computerRaiting) {
            case '2': totalSales += 0; break;
            case '3': totalSales += possibleSales * 0.5; break;
            case '4': totalSales += possibleSales * 0.7; break;
            case '5': totalSales += possibleSales * 0.85; break;
            case '6': totalSales += possibleSales; break;
        }

    }

    let averageRaiting = totalRaiting / computerCount;
    console.log(totalSales.toFixed(2));
    console.log(averageRaiting.toFixed(2));
}

computerFirm(["3",
"103",
"103",
"103"])

computerFirm(["5",
"122",
"156",
"202",
"214",
"185"])

computerFirm(["2",
"204",
"206"])

