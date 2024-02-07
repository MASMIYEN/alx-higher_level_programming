#!/usr/bin/node
const filesys = require('fs');
const file = process.argv[2];
const text = process.argv[3];
try {
  filesys.writeFileSync(file, text, 'utf8');
} catch (err) {
  console.error(err);
}
