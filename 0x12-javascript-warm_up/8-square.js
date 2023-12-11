#!/usr/bin/node
const { argv } = require('process');
const str = 'X';
const x = parseInt(argv[2], 10);
if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
        console.log(str.repeat(X));
    }
} else console.log('Missing size');