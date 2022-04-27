function areaOfFigures(input) {
    let typeOfFigure = input[0];
    let area = 0;

    if (typeOfFigure === 'square') {
        let length = Number(input[1]);
        area = length * length;
    }else if (typeOfFigure === 'rectangle') {
        let firstLength = Number(input[1]);
        let secondLength = Number(input[2]);
        area = firstLength * secondLength;
    }else if (typeOfFigure === 'circle') {
        let radius = Number(input[1]);
        area = Math.PI * radius * radius;
    }else {
        let triangleLength = Number(input[1]);
        let triangleHeight = Number(input[2]);
        area = triangleLength * triangleHeight / 2;
    }

    console.log(area.toFixed(3));
}

areaOfFigures(["square", "5"])
areaOfFigures(["rectangle", "7", "2.5"])
areaOfFigures(["circle", "6"])
areaOfFigures(["triangle", "4.5", "20"])
