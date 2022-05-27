function movieRatings(input) {
    let index = 0;
    let numbersOfMovie = Number(input[index]);
    index++;

    let bestMovieName = '';
    let bestMovieRating = Number.MIN_SAFE_INTEGER;
    let worstMovieName = '';
    let worstMovieRating = Number.MAX_SAFE_INTEGER;
    let allMovieRating = 0;

    for(let i = 1; i <= numbersOfMovie; i++) {
        let movieName = input[index];
        index++;
        let movieRating = Number(input[index]);
        index++;

        allMovieRating += movieRating;

        if(movieRating > bestMovieRating) {
            bestMovieName = movieName;
            bestMovieRating = movieRating;
        } else if (movieRating < worstMovieRating) {
            worstMovieName = movieName;
            worstMovieRating = movieRating;
        }
    }

    let averageMovieRating = allMovieRating / numbersOfMovie;

    console.log(`${bestMovieName} is with highest rating: ${bestMovieRating.toFixed(1)}`);
    console.log(`${worstMovieName} is with lowest rating: ${worstMovieRating.toFixed(1)}`);
    console.log(`Average rating: ${averageMovieRating.toFixed(1)}`);
}

movieRatings(["5",
"A Star is Born",
"7.8",
"Creed 2",
"7.3",
"Mary Poppins",
"7.2",
"Vice",
"7.2",
"Captain Marvel",
"7.1"])

movieRatings(["3",
"Interstellar",
"8.5",
"Dangal",
"8.3",
"Green Book",
"8.2"])
