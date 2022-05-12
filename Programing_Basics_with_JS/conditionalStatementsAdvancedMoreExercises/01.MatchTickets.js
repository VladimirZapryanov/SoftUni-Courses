function matchTickets(input) {
    let budget = Number(input[0]);
    let ticketType = input[1];
    let peopleInGroup = Number(input[2]);

    let transportPrice = 0;
    let vipTicketPrice = 499.99;
    let normalTicketPrice = 249.99;

    if (peopleInGroup <= 4) {
        transportPrice = budget * 0.75;
    } else if (peopleInGroup <= 9) {
        transportPrice = budget * 0.60;
    } else if (peopleInGroup <= 24) {
        transportPrice = budget * 0.50;
    } else if (peopleInGroup <= 49) {
        transportPrice = budget * 0.40;
    } else {
        transportPrice = budget * 0.25;
    }

    let budgetForTickets = budget - transportPrice;
    let allTicketsPrice = 0;

    if (ticketType === 'VIP') {
        allTicketsPrice = peopleInGroup * vipTicketPrice;
    } else {
        allTicketsPrice = peopleInGroup * normalTicketPrice;
    }

    let ticketPriceDiff = Math.abs(budgetForTickets - allTicketsPrice);

    if (budgetForTickets >= allTicketsPrice) {
        console.log(`Yes! You have ${ticketPriceDiff.toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${ticketPriceDiff.toFixed(2)} leva.`);
    }
}

matchTickets(['1000', 'Normal', '1'])
matchTickets(['30000', 'VIP', '49'])