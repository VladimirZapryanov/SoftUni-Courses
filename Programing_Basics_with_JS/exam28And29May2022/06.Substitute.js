function substitute(input) {
    let firstNumberOfFirstStart = Number(input[0]);
    let secondNumberOfFirstEnd = Number(input[1]);
    let firrstNumberOfSecondStart = Number(input[2]);
    let secondNumberOfSecondEnd = Number(input[3]);

    let substituteCount = 0;

    let isFinish = false;

    for(let k = firstNumberOfFirstStart; k <= 8; k++) {
        if(isFinish) {
            break;
        }
        for(let l = 9; l >= secondNumberOfFirstEnd; l--) {
            if(isFinish) {
                break;
            }
            for(let m = firrstNumberOfSecondStart; m <= 8; m++) {
                if(isFinish) {
                    break;
                }
                for(let n = 9; n >= secondNumberOfSecondEnd; n--) {
                    if(k % 2 === 0 && l % 2 === 1 && m % 2 === 0 && n % 2 === 1) {
                        if(`${k}${l}` !== `${m}${n}`) {
                            substituteCount++;
                            console.log(`${k}${l} - ${m}${n}`);
                        } else {
                            console.log('Cannot change the same player.');
                        }

                        if(substituteCount === 6) {
                            isFinish = true;
                            break;
                        }
                    }
                }
            }
        }
    }
}

substitute(["7",
"6",
"8",
"5"])

substitute(["6",
"7",
"5",
"6"])
