#!/usr/bin/node
const axios = require("axios");

function getMovieCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  axios.get(apiUrl)
    .then((response) => {
      const movieData = response.data;
      const characters = movieData.characters;

      characters.forEach((characterUrl) => {
        axios.get(characterUrl)
          .then((response) => {
            const characterData = response.data;
            console.log(characterData.name);
          })
          .catch((error) => {
            console.log(`Failed to retrieve character data: ${error.response.status}`);
          });
      });
    })
    .catch((error) => {
      console.log(`Failed to retrieve movie data: ${error.response.status}`);
    });
}

const movieId = process.argv[2];

if (!movieId) {
  console.log("Please provide a movie ID as a command-line argument.");
} else {
  getMovieCharacters(movieId);
}
