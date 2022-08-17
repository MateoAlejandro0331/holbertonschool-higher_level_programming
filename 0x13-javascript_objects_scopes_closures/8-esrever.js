#!/usr/bin/node

exports.esrever = function (list) {
  let output = [];
  for (let i = 0; i <= list.length; i++) {
    output.push(list.pop());
  }

  return output;
};
