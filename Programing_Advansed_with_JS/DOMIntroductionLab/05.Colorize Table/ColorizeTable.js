function colorize() {
    let rows = document.querySelectorAll('tr');

    for (let row = 1; row < rows.length; row += 2) {
        rows[row].style.background = 'Teal';
    }
}