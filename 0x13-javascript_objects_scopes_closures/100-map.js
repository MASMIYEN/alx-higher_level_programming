#!/usr/bin/node
const list = require('./100-data').list;
const map = list.map((x, index) => x * index);
console.log(list);
console.log(map);
