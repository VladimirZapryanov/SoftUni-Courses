function streamOfLetters(input) {
    let index = 0;
    let command = input[index];
    index++;

    let currentMessega = '';
    let secretMessage = '';
    let letterC = false;
    let letterO = false;
    let letterN = false;

    while(command !== 'End') {
        let letter = command;

        if(letter.match(/[a-zA-Z]/i)) {
            if(letter === 'c') {
                if(letterC) {
                    currentMessega += letter;
                }
                letterC = true;
                command = input[index];
                index++;
                if(letterC && letterO && letterN) {
                    letterC = false;
                    letterN = false;
                    letterO = false;
                    secretMessage += `${currentMessega} `;
                    currentMessega = '';
                }
                continue;
            } else if (letter === 'o') {
                if(letterO) {
                    currentMessega += letter;
                }
                letterO = true;
                command = input[index];
                index++;
                if(letterC && letterO && letterN) {
                    letterC = false;
                    letterN = false;
                    letterO = false;
                    secretMessage += `${currentMessega} `;
                    currentMessega = '';
                }
                continue;
            } else if (letter === 'n') {
                if(letterN) {
                    currentMessega += letter;
                }
                letterN = true;
                command = input[index];
                index++;
                if(letterC && letterO && letterN) {
                    letterC = false;
                    letterN = false;
                    letterO = false;
                    secretMessage += `${currentMessega} `;
                    currentMessega = '';
                }
                continue;
            } else {
                currentMessega += letter;
            }
        }

        command = input[index];
        index++;
    }

    console.log(secretMessage);
}

streamOfLetters(['H', 'n', 'e', 'l', 'l', 'o', 'o', 'c', 't', 'c', 'h', 'o', 'e', 'r', 'e', 'n', 'e', 'End'])
streamOfLetters(['%', '!', 'c', '^', 'B', '`', 'o', '%', 'o', 'o', 'M', ')', '{', 'n', 'A', 'D', 'End'])
streamOfLetters(['o', 'S', '%', 'o', 'l', '^', 'V', 'e', 'c', 'n', '&', 'm', 'e', 'c', 'o', 'n', 'End'])