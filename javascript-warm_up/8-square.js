#!/usr/bin/node
const { argv } = require('node:process');
const isNum = parseInt(argv[2], 10);

if (isNaN(isNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < isNum; i++) {
    console.log('X'.repeat(isNum));
  }
}
