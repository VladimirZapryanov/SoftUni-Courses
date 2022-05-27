function agencyProfit(input) {
    let companyName = input[0];
    let adultsTickets = Number(input[1]);
    let kidsTickets = Number(input[2]);
    let adultsTicketsPrice = Number(input[3]);
    let agencyTaxes = Number(input[4]);

    let kidsTicketsPrice = adultsTicketsPrice * 0.3;
    let adultsTicketsPriceWithTaxes = adultsTicketsPrice + agencyTaxes;
    let kidsTicketsPriceWithTaxes = kidsTicketsPrice + agencyTaxes;
    let totalTicketPrice = adultsTicketsPriceWithTaxes * adultsTickets + kidsTicketsPriceWithTaxes * kidsTickets;
    let agencyProfit = totalTicketPrice * 0.2;

    console.log(`The profit of your agency from ${companyName} tickets is ${agencyProfit.toFixed(2)} lv.`);
}

agencyProfit(['WizzAir', '15', '5', '120', '40'])
agencyProfit(['Ryanair', '60', '23', '158.96', '39.12'])
