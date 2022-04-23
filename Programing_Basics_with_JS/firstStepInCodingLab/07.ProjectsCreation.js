function projectsCreation(input) {

    let neededHoursForOneProject = 3;

    let name = input[0];
    let numbersOfProjects = Number(input[1]);

    let neededHoursForAllProjects = numbersOfProjects * neededHoursForOneProject;

    console.log(`The architect ${name} will need ${neededHoursForAllProjects} hours to complete ${numbersOfProjects} project/s.`);
}

projectsCreation(["George", "4"])
projectsCreation(["Sanya ", "9"])
