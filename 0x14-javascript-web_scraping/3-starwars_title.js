#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/'
request(url + ep, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
