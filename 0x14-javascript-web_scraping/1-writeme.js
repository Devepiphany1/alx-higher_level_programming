#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Use fs.writeFile() to write data to a file specified as the third comment.

  if (error) {
    // If an error occurs during the write operation.
    console.error(error);
  }
});
