#!/usr/bin/node

exports.esrever = function (list) {
  const output = [];
  for (let i = 0; i <= list.length; i++) {
    output.push(list.pop());
  }

  return output;
};
