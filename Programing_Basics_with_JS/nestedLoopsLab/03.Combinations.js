function combination(input) {
    let finalNumber = Number(input[0]);

    let totalCount = 0;

    for(let num1 = 0; num1 <= finalNumber; num1++) {
        for(let num2 = 0; num2 <= finalNumber; num2++) {
            for(let num3 = 0; num3 <= finalNumber; num3++) {
                if(num1 + num2 + num3 === finalNumber) {
                    totalCount++;
                }
            }
        }
    }

    console.log(totalCount);
}

combination(['25'])
combination(['20'])