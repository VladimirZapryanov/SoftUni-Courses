function fueltank(input) {
    let typeOfFuel = input[0];
    let fuelLiters = Number(input[1]);

    if (typeOfFuel !== 'Diesel' && typeOfFuel !== 'Gasoline' && typeOfFuel !== 'Gas') {
        console.log('Invalid fuel!');
    } else {
        if (fuelLiters < 25) {
            console.log(`Fill your tank with ${typeOfFuel.toLowerCase()}!`);
        } else {
            console.log(`You have enough ${typeOfFuel.toLowerCase()}.`);
        }
    }
}

fueltank(['Diesel', '10'])
fueltank(['Gasoline', '40'])
fueltank(['Gas', '25'])
fueltank(['Kerosene', '200'])