#!/usr/bin/node
const request = require('request');
const parameter = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${parameter}/`,
  (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const characterList = JSON.parse(body).characters;
    characterList.forEach((element) => {
      request(element, (error, _, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
      });
    });
  }
);
