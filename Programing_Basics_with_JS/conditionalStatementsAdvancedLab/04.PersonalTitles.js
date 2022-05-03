function personalTitle(input) {
    let age = Number(input[0]);
    let gender = input[1];

    if (gender === 'f') {
        if (age < 16) {
            console.log('Miss');
        } else {
            console.log('Ms.');
        }
    } else if (gender === 'm') {
        if (age < 16) {
            console.log('Master');
        } else {
            console.log('Mr.');
        }
    }
}

personalTitle(['12', 'f'])
personalTitle(['17', 'm'])
personalTitle(['25', 'f'])
personalTitle(['13.5', 'm'])