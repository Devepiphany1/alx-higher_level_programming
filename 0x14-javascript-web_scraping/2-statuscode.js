#!/usr/bin/node

const request = require('request');
// Import 'request' module.

request.get(process.argv[2])
// Get HTTP request Using the 'request' module.

  .on('response', function (response) {
    // Set up an event listener for the 'response' event

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });
