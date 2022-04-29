function trainingLab(input) {
    let widthInMeters = Number(input[0]);
    let heightInMeters = Number(input[1]);

    let lostPlaceForDoor = 1;
    let lostPlaceForDepartment = 2;
    let lastSpaceForCorridor = 100;

    let widthInCantimeters = widthInMeters * 100;
    let heightInCantimeters = heightInMeters * 100;
    let freeSpaceHeight = Math.floor((heightInCantimeters - lastSpaceForCorridor) / 70); 
    let freeSpaceWidth = Math.floor(widthInCantimeters / 120);
    let allPlaces = freeSpaceHeight * freeSpaceWidth - lostPlaceForDoor - lostPlaceForDepartment;

    console.log(allPlaces);
}

trainingLab(["8.4", "5.2"])
trainingLab(["15", "8.9"])