function fishTank(input) {
    let lengthInCm = Number(input[0]);
    let widthInCm = Number(input[1]);
    let heightInCm = Number(input[2]);
    let persentageOfDust = Number(input[3]);

    let parallelepipedAreaInCm = lengthInCm * heightInCm * widthInCm;
    let freeAreaForWater = parallelepipedAreaInCm - parallelepipedAreaInCm * (persentageOfDust / 100);
    let neededWater = freeAreaForWater / 1000;

    console.log(neededWater);
}

fishTank(["85", "75", "47", "17"])
fishTank(["105", "77", "89", "18.5"])