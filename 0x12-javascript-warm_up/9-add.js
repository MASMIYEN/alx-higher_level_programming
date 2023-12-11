#!/usr/bin/node
const { argv } = require('process');
const i = parseInt(argv[2], 10);
const j = parseInt(argv[3], 10);
function add (i, j) {
  return i + j;
}
console.log(add(i, j));
