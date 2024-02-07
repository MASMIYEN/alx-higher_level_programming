#!/usr/bin/node
const filesys = require('fs');
const file = process.argv[2];
try {
  const data = filesys.readFileSync(file, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
