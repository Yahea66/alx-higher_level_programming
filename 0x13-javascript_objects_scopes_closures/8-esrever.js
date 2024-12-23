#!/usr/bin/node

exports.esrever = function (list) {
  const iter = parseInt((list.length / 2));
  let indx = list.length - 1;
  for (let i = 0; i < iter; i++) {
    const temp = list[indx];
    list[indx] = list[i];
    list[i] = temp;
    indx -= 1;
  }
  return list;
};
