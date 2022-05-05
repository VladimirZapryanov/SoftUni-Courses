function cinema(input) {
    let ticketType = input[0];
    let rowCount = Number(input[1]);
    let colCount = Number(input[2]);

    let totalCapacity = rowCount * colCount;
    let totalMoney = 0;
    let premiereTicketPrice = 12.00;
    let normalTicketPrice = 7.50;
    let discountTicketPrice = 5.00;

    switch(ticketType) {
        case 'Premiere': totalMoney = totalCapacity * premiereTicketPrice; break;
        case 'Normal': totalMoney = totalCapacity * normalTicketPrice; break;
        case 'Discount': totalMoney = totalCapacity * discountTicketPrice; break;
    }
    console.log(`${totalMoney.toFixed(2)} leva`)
}

cinema(["Premiere",
"10",
"12"])

cinema(["Normal",
"21",
"13"])

cinema(["Discount",
"21",
"13"])

