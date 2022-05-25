function footballLeague(input) {
    let index = 0;
    let totalCapacity = Number(input[index]);
    index++;
    let allFans = Number(input[index]);
    index++;

    let sectorA = 0;
    let sectorB = 0;
    let sectorV = 0;
    let sectorG = 0;

    for(let i = 1; i <= allFans; i++) {
        let fanSector = input[index];
        index++;

        switch(fanSector) {
            case 'A': sectorA++; break;
            case 'B': sectorB++; break;
            case 'V': sectorV++; break;
            case 'G': sectorG++; break;
        }
    }

    let sectorAPercent = sectorA / allFans * 100;
    let sectorBPercent = sectorB / allFans * 100;
    let sectorVPercent = sectorV / allFans * 100;
    let sectorGPercent = sectorG / allFans * 100;
    let allFansPercent = allFans / totalCapacity * 100;

    console.log(`${sectorAPercent.toFixed(2)}%`);
    console.log(`${sectorBPercent.toFixed(2)}%`);
    console.log(`${sectorVPercent.toFixed(2)}%`);
    console.log(`${sectorGPercent.toFixed(2)}%`);
    console.log(`${allFansPercent.toFixed(2)}%`);
}

footballLeague(['76', '10', 'A', 'V', 'V', 'V', 'G', 'B', 'A', 'V', 'B', 'B'])
footballLeague(['1000', '12', 'A', 'A', 'V', 'V', 'A', 'G', 'A', 'A', 'V', 'G', 'V', 'A'])
footballLeague(['93', '16', 'A', 'V', 'G', 'G', 'B', 'B', 'G', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A'])