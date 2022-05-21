function oldBooks(input) {
    let index = 0;
    let searchedBook = input[index];
    index++;
    let command = input[index];
    index++;

    let checkedBook = 0;
    let bookIsFound = false;

    while(command !== 'No More Books') {
        checkedBook++;
        let findBook = command;

        if (findBook === searchedBook) {
            bookIsFound = true;
            checkedBook--;
            break;
        }

        command = input[index];
        index++;
    }

    if(bookIsFound) {
        console.log(`You checked ${checkedBook} books and found it.`);
    } else {
        console.log('The book you search is not here!');
        console.log(`You checked ${checkedBook} books.`);
    }
}

oldBooks(["Troy",
"Stronger",
"Life Style",
"Troy"])

oldBooks(["The Spot",
"Hunger Games",
"Harry Potter",
"Torronto",
"Spotify",
"No More Books"])

oldBooks(["Bourne",
"True Story",
"Forever",
"More Space",
"The Girl",
"Spaceship",
"Strongest",
"Profit",
"Tripple",
"Stella",
"The Matrix",
"Bourne"])


