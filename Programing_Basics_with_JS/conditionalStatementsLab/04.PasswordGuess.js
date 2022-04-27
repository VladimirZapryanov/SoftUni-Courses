function passwordGuess(input) {
    let password = "s3cr3t!P@ssw0rd";
    let successMessage = "Welcome";
    let wrongMessage = "Wrong password!";
    let inputPassword = input[0];

    if (password === inputPassword) {
        console.log(`${successMessage}`);
    }else {
        console.log(`${wrongMessage}`);
    }
}

passwordGuess(["qwerty"])
passwordGuess(["s3cr3t!P@ssw0rd"])
passwordGuess(["s3cr3t!p@ss"])