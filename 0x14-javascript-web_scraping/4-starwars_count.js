#!/usr/bin/node

const request = require('request');
const film = process.argv[2];
const url = film.replace('films', 'people/18');

request(url, function (error, _, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.films.length);
  }
});
