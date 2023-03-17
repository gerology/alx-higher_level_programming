#!/usr/bin/node
function factorial (f) {
  if (isNaN(f) || f === 0) {
    return 1;
  } else {
    return f * factorial(f - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
