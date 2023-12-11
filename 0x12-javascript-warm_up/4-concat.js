#!/usr/bin/node
const { argv } = require ('process');
const firstArg = argv[2];
const secondArg = argv[3];
const midArg = ' is ';
console.log(firstArg + midArg + secondArg);
