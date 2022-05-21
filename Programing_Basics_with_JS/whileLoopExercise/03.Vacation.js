function vacation(input) {
    let index = 0;
    let vacationPrice = Number(input[index]);
    index++;
    let money = Number(input[index]);
    index++;

    let days = 0;
    let spendDays = 0;
    let youSaveMoney = false;

    while(spendDays < 5) {
        days++;
        let command = input[index];
        index++;
        let currentMoney = Number(input[index]);
        index++;

        if (command === 'spend') {
            spendDays++;
            money -= currentMoney;
            if (money < 0) {
                money = 0;
            }
        } else if (command === 'save') {
            money += currentMoney;
            spendDays = 0;
        }

        if (money >= vacationPrice) {
            youSaveMoney = true;
            break;
        }
    }
    
    if (youSaveMoney) {
        console.log(`You saved the money for ${days} days.`);
    } else {
        console.log(`You can't save the money.`);
        console.log(`${days}`);
    }
}

vacation(["2000",
"1000",
"spend",
"1200",
"save",
"2000"])

vacation(["110",
"60",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10"])
