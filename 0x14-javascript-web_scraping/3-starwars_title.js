#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, function (error, _, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
