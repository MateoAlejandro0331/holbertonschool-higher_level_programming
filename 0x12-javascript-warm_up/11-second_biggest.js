#!/usr/bin/node

process.argv.shift();
process.argv.shift();
const len = process.argv.length;
/* for (let i = 0; i < len - 2; i++) {
  process.argv[i] = parseInt(process.argv[i]);
} */
process.argv.sort((a, b) => a - b);
console.log(process.argv[len - 2]);
