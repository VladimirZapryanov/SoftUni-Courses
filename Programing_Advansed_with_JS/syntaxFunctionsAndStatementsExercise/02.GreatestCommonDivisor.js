function GCD(num1, num2) {
    if(num2) {
        return GCD(num2, num1 % num2);
    } else {
        console.log(num1);
    }
}

GCD(15, 5)
GCD(2154 , 458)