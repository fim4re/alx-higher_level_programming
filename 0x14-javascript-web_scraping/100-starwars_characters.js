#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const ab = JSON.parse(body);
  const dd = ab.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const ab1 = JSON.parse(body1);
      console.log(ab1.name);
    });
  }
});
