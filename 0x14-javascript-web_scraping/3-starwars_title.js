#!/usr/bin/node

// Import 'request' module.
const request = require('request');

// Construct the URL
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

  // log title if successful, log error if not.
  console.log(error || JSON.parse(body).title);
});
