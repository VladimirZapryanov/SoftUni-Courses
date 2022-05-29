function excursion(input) {
    let peopleInGroup = Number(input[0]);
    let nightCount = Number(input[1]);
    let transportCards = Number(input[2]);
    let museumTickets = Number(input[3]);

    let nightPrice = 20;
    let transportCardsPrice = 1.60;
    let museumTicketsPrice = 6;

    let allNightPrice = nightCount * nightPrice;
    let allTransportCardsPrice = transportCards * transportCardsPrice;
    let allMuseumTicketsPrice = museumTickets * museumTicketsPrice;

    let costForOnePerson = allNightPrice + allTransportCardsPrice + allMuseumTicketsPrice;
    let costForAllPeople = costForOnePerson * peopleInGroup;
    let totalCost = costForAllPeople * 1.25;

    console.log(totalCost.toFixed(2));
}

excursion(["20",
"14",
"30",
"6"])

excursion(["131",
"9",
"33",
"46"])
