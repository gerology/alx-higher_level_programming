#!/usr/bin/node

if (process.argv.length <= 3) {
  return 0;
} else {
  const val = process.argv.map(Number)
  .slice(2, process.argv.lenth)
  .sort((a, b) => a -b);
  console.log(val[val.length - 2]);
}