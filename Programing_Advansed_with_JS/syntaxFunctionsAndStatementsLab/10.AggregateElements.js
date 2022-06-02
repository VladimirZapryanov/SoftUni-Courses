function aggregateElement(input) {
    let index =0;
    let length = input.length;

    let sum = 0;
    let inverseSum = 0;
    let concat = '';

    for(let i = 1; i <= length; i++) {
        let number = Number(input[index]);
        let stringNum = number + "";
        index++;
        sum += number;
        inverseSum += 1 / number;
        concat += stringNum;
    }
    

    console.log(sum);
    console.log(inverseSum);
    console.log(concat);
}

aggregateElement([1, 2, 3])
aggregateElement([2, 4, 8, 16])

