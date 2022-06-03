function evenPositionElement(input) {
    let result = '';
    let elementLength = input.length;

    for (let i = 0; i < elementLength; i++) {
        if (i % 2 == 0) {
            result += `${input[i]} `;
        }
    }

    console.log(result);
}

evenPositionElement(['20', '30', '40', '50', '60'])
evenPositionElement(['5', '10'])