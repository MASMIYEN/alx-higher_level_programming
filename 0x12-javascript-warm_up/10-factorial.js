#!/usr/bin/node
const { argv } = require('process');
const i = parseInt(argv[2], 10);
function factorial (i) {
    if (i <= 1) return 1;
    return i * factorial(i - 1);
}
if (isNaN(i)) console.log(1);
else console.log(factorial(i));