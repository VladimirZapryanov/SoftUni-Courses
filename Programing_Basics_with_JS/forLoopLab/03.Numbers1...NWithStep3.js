function numbers(input) {
    let number = Number(input[0]);

    for (let i = 1; i <= number; i+=3) {
        console.log(i);
    }
}

numbers(['10'])
numbers(['7'])
numbers(['15'])