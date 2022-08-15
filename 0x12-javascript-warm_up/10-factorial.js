#!/usr/bin/node

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

let num = 0;

num = factorial(Number(process.argv[2]));
console.log(num);
