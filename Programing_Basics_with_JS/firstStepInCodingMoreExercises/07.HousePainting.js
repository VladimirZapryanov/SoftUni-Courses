function housePainting(input) {
    let houseHeight = Number(input[0]);
    let houseLength = Number(input[1]);
    let coverHeight = Number(input[2]);

    let greenPaintLitters = 0;
    let redPaintLitters = 0;
    let neededGreenPainPerMetter = 3.4;
    let neededRedPainPerMetter = 4.3;

    let doorArea = 1.2 * 2;
    let frontWallArea = houseHeight * houseHeight - doorArea;
    let rearWallArea = houseHeight * houseHeight;
    let windowsArea = (1.5 * 1.5) * 2;
    let sidesWallArea = (houseHeight * houseLength) * 2 - windowsArea;

    let sidesCoverArea = (houseHeight * houseLength) * 2;
    let theRestOfCover = coverHeight * houseHeight;

    redPaintLitters += (sidesCoverArea + theRestOfCover) / neededRedPainPerMetter;
    greenPaintLitters += (frontWallArea + rearWallArea + sidesWallArea) / neededGreenPainPerMetter;

    console.log(greenPaintLitters.toFixed(2));
    console.log(redPaintLitters.toFixed(2));
}

housePainting(["6", "10", "5.2"])
housePainting(["10.25", "15.45", "8.88"])