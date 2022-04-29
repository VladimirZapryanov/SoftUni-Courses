function weatherForecast(input) {
    let temperature = input[0];

    let message = " ";

    if (temperature >= 5 && temperature < 12) {
        message = "Cold";
    } else if (temperature >= 12 && temperature < 15) {
        message = "Cool";
    } else if (temperature >= 15 && temperature <= 20) {
        message = "Mild";
    } else if (temperature >= 20.1 && temperature < 26) {
        message = "Warm";
    } else if (temperature >= 26 && temperature <= 35) {
        message = "Hot";
    } else {
        message = "unknown";
    }

    console.log(message);
}

weatherForecast(["16.5"])
weatherForecast(["8"])
weatherForecast(["22.4"])
weatherForecast(["26"])
weatherForecast(["0"])
