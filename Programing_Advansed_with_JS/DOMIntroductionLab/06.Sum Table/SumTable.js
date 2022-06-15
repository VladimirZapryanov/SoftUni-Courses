function sumTable() {
    let totalCost = 0;
    let rows = document.getElementsByTagName('td');

    for (let el = 1; el < rows.length - 1; el += 2) {
        totalCost += Number(rows[el].textContent);
    }

    document.getElementById('sum').textContent = totalCost;
}