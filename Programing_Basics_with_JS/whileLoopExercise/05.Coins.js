function coins(input) {
    let moneyInBgn = Number(input[0]);

    let money = Math.floor(moneyInBgn * 100); 
    let coins = 0;

    while(money > 0) {
        coins++;
        if (money >= 200) {
            money -= 200;
        } else if (money >= 100) {
            money -= 100;
        } else if (money >= 50) {
            money -= 50;
        } else if (money >= 20) {
            money -= 20;
        } else if (money >= 10) {
            money -= 10;
        } else if (money >= 5) {
            money -= 5;
        } else if (money >= 2) {
            money -= 2;
        } else {
            money -= 1;
        }
    }

    console.log(coins);
}

coins(['1.23'])
coins(['2'])
coins(['0.56'])
coins(['2.73'])