function celsiusToFahrenheit(input) {
    let temperatureInC = Number(input[0]);

    let temperatureInF = temperatureInC * 1.8 + 32;

    console.log(temperatureInF.toFixed(2));
}

celsiusToFahrenheit(["25"])
celsiusToFahrenheit(["0"])
celsiusToFahrenheit(["-5.5"])
celsiusToFahrenheit(["32.3"])