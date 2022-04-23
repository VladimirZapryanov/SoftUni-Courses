function petShop(input) {

    let foodPriceForDog = 2.5;
    let foodPriceForCat = 4;

    let numberOfDogFoodPackages = Number(input[0]);
    let numberOfCatFoodPackages = Number(input[1]);

    let totalPrice = foodPriceForDog * numberOfDogFoodPackages + foodPriceForCat * numberOfCatFoodPackages;

    console.log(`${totalPrice} lv.`)
}

petShop(["5", "4"])
petShop(["13", "9"])