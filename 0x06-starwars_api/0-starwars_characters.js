const request = require('request');

function getMovieCharacters(movieId) {
    const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
    
    request(apiUrl, (error, response, body) => {
        if (response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const characters = movieData.characters;
            
            characters.forEach((characterUrl) => {
                request(characterUrl, (error, response, body) => {
                    if (response.statusCode === 200) {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                    } else {
                        console.log(`Failed to retrieve character data: ${response.statusCode}`);
                    }
                });
            });
        } else {
            console.log(`Failed to retrieve movie data: ${response.statusCode}`);
        }
    });
}

const movieId = process.argv[2];

if (!movieId) {
    console.log("Please provide a movie ID as a command-line argument.");
} else {
    getMovieCharacters(movieId);
}
