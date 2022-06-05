function addRemoveElement(array) {
    let count = 0;
    let length = array.length;
    let newArray = [];

    for (let i = 0; i < length; i++) {
        let command = array[i];
        count++;
        switch (command) {
            case 'add': newArray.push(count); break;
            case 'remove': newArray.pop(); break;
        }
    }

    if (newArray.length > 0) {
        console.log(newArray.join('\n'));
    } else {
        console.log('Empty');
    }
}

addRemoveElement(['add',
    'add',
    'add',
    'add']
)

addRemoveElement(['add',
    'add',
    'remove',
    'add',
    'add']
)

addRemoveElement(['remove',
    'remove',
    'remove']
)