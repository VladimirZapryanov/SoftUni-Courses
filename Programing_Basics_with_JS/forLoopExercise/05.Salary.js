function salary(input) {
    let index = 0;
    let numbersOfOpenTabs = Number(input[index]);
    index++;
    let salary = Number(input[index]);
    index++;
    let lostSalary = false;

    for (let i = 1; i <= numbersOfOpenTabs; i++) {
        let openTab = input[index];
        index++;

        switch(openTab) {
            case 'Facebook': salary -= 150; break;
            case 'Instagram': salary -= 100; break;
            case 'Reddit': salary -= 50; break;
        }

        if (salary <= 0) {
            lostSalary = true;
            console.log('You have lost your salary.');
            break;
        }
    }
    if (salary) {
        console.log(Math.trunc(salary));
    }
}

salary(["10",
"750",
"Facebook",
"Dev.bg",
"Instagram",
"Facebook",
"Reddit",
"Facebook",
"Facebook"])

salary(["3",
"500",
"Github.com",
"Stackoverflow.com",
"softuni.bg"])
