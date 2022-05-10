function vowelsSum(input) {
    let text = input[0];

    let sum = 0;
    let textLength = text.length;

    for (let i = 0; i < textLength; i++) {
        switch(text[i]) {
            case 'a': sum += 1; break;
            case 'e': sum += 2; break;
            case 'i': sum += 3; break;
            case 'o': sum += 4; break;
            case 'u': sum += 5; break;
        }
    }

    console.log(sum);
}

vowelsSum(['hello'])
vowelsSum(['hi'])
vowelsSum(['bamboo'])
vowelsSum(['beer'])