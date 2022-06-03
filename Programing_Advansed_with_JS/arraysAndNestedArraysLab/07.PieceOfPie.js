function pieceOfPie(array, startPie, endPie) {
    let startIndex = array.indexOf(startPie);
    let endIndex = array.indexOf(endPie) + 1;

    let searchedPies = array.slice(startIndex, endIndex);
    return searchedPies;
}

console.log(pieceOfPie(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'
))

console.log(pieceOfPie(['Apple Crisp',
'Mississippi Mud Pie',
'Pot Pie',
'Steak and Cheese Pie',
'Butter Chicken Pie',
'Smoked Fish Pie'],
'Pot Pie',
'Smoked Fish Pie'
))