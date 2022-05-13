function multiplyByTwo(input) {
    let index = 0;
    let number = Number(input[index]);
    index++;

    while (number >= 0) {
        result = number * 2;
        console.log(`Result: ${result.toFixed(2)}`);
        
        number = Number(input[index]);
        index++;
    }

    console.log('Negative number!');
}

multiplyByTwo(['12', '43.2144', '12.3', '543.23', '-20'])
multiplyByTwo(['23.43', '12.3245', '0', '65.23432', '23', '65', '-12'])
multiplyByTwo(['-123'])