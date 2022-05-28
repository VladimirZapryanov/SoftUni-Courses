function easterLunch(input) {
    let easterCakes = Number(input[0]);
    let eggs = Number(input[1]);
    let cookies = Number(input[2]);

    let easterCakesPrice = 3.20;
    let eggsPrice = 4.35;
    let cookiesPrice = 5.40;
    let eggsPaint = 0.15;

    let allEasterCakesPrice = easterCakes * easterCakesPrice;
    let paintEggsPrice = eggs * 12 * eggsPaint;
    let allEggsPrice = eggs * eggsPrice + paintEggsPrice;
    let allCookiesPrice = cookies * cookiesPrice;

    let totalCost = allEasterCakesPrice + allEggsPrice + allCookiesPrice;
    console.log(totalCost.toFixed(2));
}

easterLunch(["3",
"2",
"3"])

easterLunch(["4",
"4",
"3"])

easterLunch(["2",
"3",
"2"])

