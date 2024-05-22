#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const d = JSON.parse(body);
  const dd = d.characters;
  for (const i of dd) {
    request.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const d1 = JSON.parse(body1);
      console.log(d1.name);
    });
  }
});
