#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 3) {
  console.log(0);
} else {
  let biggestNum = parseInt(argv[2], 10);
  let scndBiggestNum = 0;

  argv.slice(3).forEach((val) => {
    const num = parseInt(val, 10);
    if (num > biggestNum) {
      scndBiggestNum = biggestNum;
      biggestNum = num;
    } else if (num > scndBiggestNum) {
      scndBiggestNum = num;
    }
  });
  console.log(scndBiggestNum);
}
