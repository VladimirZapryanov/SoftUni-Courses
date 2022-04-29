function weatherForecast(input) {
    let weather = input[0];

    let message = ''

    if (weather === "sunny") {
        message = "It's warm outside!";
    } else {
        message = "It's cold outside!";
    }

    console.log(message);
}

weatherForecast(["sunny"])
weatherForecast(["cloudy"])
weatherForecast(["snowy"])