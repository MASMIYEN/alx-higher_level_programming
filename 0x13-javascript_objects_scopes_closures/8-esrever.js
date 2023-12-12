#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (const elem of list) {
    reverse.unshift(elem);
  }
  return reverse;
};
