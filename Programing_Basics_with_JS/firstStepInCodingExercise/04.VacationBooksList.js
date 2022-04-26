function vacationBookList(input) {
    let pagesCount = Number(input[0]);
    let pagesReadInOneHour = Number(input[1]);
    let daysCount = Number(input[2]);

    let housrForAllPages = pagesCount / pagesReadInOneHour;
    let neededHoursPerDay = housrForAllPages / daysCount;

    console.log(neededHoursPerDay);
}

vacationBookList(["212", "20", "2"])
vacationBookList(["432", "15", "4"])