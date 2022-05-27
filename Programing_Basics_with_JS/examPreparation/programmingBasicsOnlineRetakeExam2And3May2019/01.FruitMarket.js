function fruitMarker(input) {
    let strawberryPrice = Number(input[0]);
    let kilogramsOfBanana = Number(input[1]);
    let kilogramsOfOranges = Number(input[2]);
    let kilogramsOfRaspberry = Number(input[3]);
    let kilogramsOfStrawberry = Number(input[4]);

    let raspberryPrice = strawberryPrice * 0.5;
    let orangesPrice = raspberryPrice * 0.6;
    let bananaPrice = raspberryPrice * 0.2;

    let totalNeededMoney = strawberryPrice * kilogramsOfStrawberry + bananaPrice * kilogramsOfBanana + orangesPrice * kilogramsOfOranges + raspberryPrice * kilogramsOfRaspberry;

    console.log(totalNeededMoney.toFixed(2));
}

fruitMarker(['48', '10', '3.3', '6.5', '1.7'])
fruitMarker(['63.5', '3.57', '6.35', '8.15', '2.5'])