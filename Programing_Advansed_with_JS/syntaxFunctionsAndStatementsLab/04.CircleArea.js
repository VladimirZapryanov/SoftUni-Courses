function circleArea(arg1) {
    let type = typeof(arg1);
    
    if(type === "number") {
        console.log((Math.pow(arg1, 2) * Math.PI).toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${type}.`);
    }
}

circleArea(5)
circleArea('name')