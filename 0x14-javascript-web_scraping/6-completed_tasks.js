#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const tod = JSON.parse(body);
    const complet = {};
    tod.forEach((todo) => {
      if (todo.complet && complet[todo.userId] === undefined) {
        complet[todo.userId] = 1;
      } else if (todo.complet) {
        complet[todo.userId] += 1;
      }
    });
    console.log(complet);
  }
});
