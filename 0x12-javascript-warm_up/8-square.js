#!/usr/bin/node

const myVar = 'X';

if (Number(process.argv[2])) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log(myVar.repeat(Number(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
