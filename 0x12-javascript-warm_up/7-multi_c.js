#!/usr/bin/node
const { argv } = require('process');
const str = 'C is fun';
let x = parseInt(argv[2], 10);
if (!isNaN(x)) {
  while (x > 0) {
      console.log(str);
      x--;
  }
} else console.log('Misssing number of occurences');
