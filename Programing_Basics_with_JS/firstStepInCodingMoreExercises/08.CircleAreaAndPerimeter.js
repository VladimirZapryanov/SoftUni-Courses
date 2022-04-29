function circleAreaAndPerimeter(input) {
    let radius = Number(input[0]);

    let circleArea = radius * radius * Math.PI;
    let perimeter = radius * 2 * Math.PI;

    console.log(circleArea.toFixed(2));
    console.log(perimeter.toFixed(2));
}

circleAreaAndPerimeter(["3"])
circleAreaAndPerimeter(["4.5"])