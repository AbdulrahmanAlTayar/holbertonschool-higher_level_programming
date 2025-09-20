#!/usr/bin/node
const { argv } = require('node:process');
const isNum = parseInt(argv[2], 10);

function fact (num) {
  if (num <= 0 || isNaN(num)) {
    return 1;
  }
  return num * fact(num - 1);
}

console.log(fact(isNum));
