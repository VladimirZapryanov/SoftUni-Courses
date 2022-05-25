function equalPairs(input) {
    const n = Number(input[0]);
    const firstSum = Number(input[1]) + Number(input[2]);
    let currentSum = 0;
    let difference = 0;
    let maxDiff = 0;
    let isEqual = false;
   
    if (n === 1) {
      console.log(`Yes, value=${firstSum}`);
    } else {
      for (let i = 3; i <= 2 * n; i += 2) {
        currentSum = +input[i] + +input[i + 1];
        if (firstSum === currentSum) {
          isEqual = true;
        } else {
          difference = Math.abs(+input[i - 2] + +input[i - 1] - currentSum);
        }
        if (difference >= maxDiff) {
          maxDiff = difference;
        }
      }
      if (isEqual === false) {
        console.log(`No, maxdiff=${maxDiff}`);
      } else {
        console.log(`Yes, value=${firstSum}`);
      }
    }
  }

equalPairs(['3', '1', '2', '0', '3', '4', '-1'])
equalPairs(['4', '1', '1', '3', '1', '2', '-2', '0', '0'])
equalPairs(['2', '-1', '0', '0', '-1'])
equalPairs(['2', '1', '2', '2', '2'])
equalPairs(['1', '5', '5'])
equalPairs(['2', '-1', '2', '0', '-1'])
equalPairs([7,
    34,
    -33,
    52,
    12,
    -32,
    32,
    23,
    41,
    7,
    25,
    34,
    23,
    124,
    21])
