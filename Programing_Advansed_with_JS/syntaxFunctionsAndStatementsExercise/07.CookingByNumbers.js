function cookingByNumbers(number, ...command) {
    let commandLength = command.length;

    for (let i = 0; i < commandLength; i++) {
        let currentCommand = command[i];
        number = Number(number);

        switch (currentCommand) {
            case 'chop': number = number / 2; break;
            case 'dice': number = Math.sqrt(number); break;
            case 'spice': number++; break;
            case 'bake': number = number * 3; break;
            case 'fillet': number = (number * 0.8).toFixed(1); break
        }

        console.log(number);
    }
}

cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet')
