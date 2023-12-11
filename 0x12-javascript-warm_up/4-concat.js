#!/usr/bin/node
const { arg } = require ('process');
const firstArg = argv[2];
const secondArg = arg[3];
const midArg = ' is ';
console.log(firstArg + midArg + secondArg);
