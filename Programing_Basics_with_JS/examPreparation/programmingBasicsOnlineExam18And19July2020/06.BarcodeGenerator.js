function barcodeGenerator(input) {
    let firstBarcode = input[0];
    let lastBarcode = input[1];

    let firstNumberStart = Number(firstBarcode[0]);
    let firstNumberEnd = Number(lastBarcode[0]);
    let secondNumberStart = Number(firstBarcode[1]);
    let secondNumberEnd = Number(lastBarcode[1]);
    let thirdNumberStart = Number(firstBarcode[2]);
    let thirdNumberEnd = Number(lastBarcode[2]);
    let fourthNumberStart = Number(firstBarcode[3]);
    let fourthNumberEnd = Number(lastBarcode[3]);

    let allNeededBarcodes = '';

    for(let num1 = firstNumberStart; num1 <= firstNumberEnd; num1++) {
        for(let num2 = secondNumberStart; num2 <= secondNumberEnd; num2++) {
            for(let num3 = thirdNumberStart; num3 <= thirdNumberEnd; num3++) {
                for(let num4 = fourthNumberStart; num4 <= fourthNumberEnd; num4++) {
                    if(num1 % 2 === 1 && num2 % 2 === 1 && num3 % 2 === 1 && num4 % 2 === 1) {
                        allNeededBarcodes += (`${num1}${num2}${num3}${num4} `);
                    }
                }
            }
        }
    }

    console.log(allNeededBarcodes);
}

barcodeGenerator(['2345', '6789'])
barcodeGenerator(['3256', '6579'])
barcodeGenerator(['1365', '5877'])