function bills(input) {
    let index = 0;
    let numbersOfMonth = Number(input[index]);
    index++;

    let waterBillPerMonth = 20;
    let internetBillPerMonth = 15;
    let totalWaterBill = waterBillPerMonth * numbersOfMonth;
    let totalInternetBill = internetBillPerMonth * numbersOfMonth;
    let totalElectricityBill = 0;
    let totalOtherBill = 0;
    
    for(let i = 1; i <= numbersOfMonth; i++) {
        let electricityBillPerMonth = Number(input[index]);
        index++;
        totalElectricityBill += electricityBillPerMonth;
        let otherBillPerMonth = (waterBillPerMonth + internetBillPerMonth + electricityBillPerMonth) * 1.2;
        totalOtherBill += otherBillPerMonth;
    }

    let averageBillPerMonth = (totalWaterBill + totalInternetBill + totalElectricityBill + totalOtherBill) / numbersOfMonth;

    console.log(`Electricity: ${totalElectricityBill.toFixed(2)} lv`);
    console.log(`Water: ${totalWaterBill.toFixed(2)} lv`);
    console.log(`Internet: ${totalInternetBill.toFixed(2)} lv`);
    console.log(`Other: ${totalOtherBill.toFixed(2)} lv`);
    console.log(`Average: ${averageBillPerMonth.toFixed(2)} lv`);
}

bills(['5', '68.63', '89.25', '132.53', '93.53', '63.22'])
bills(['8', '123.54', '231.54', '140.23', '100', '122.4', '430', '178.52', '64.2'])