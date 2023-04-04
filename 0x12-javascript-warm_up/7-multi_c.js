#!/usr/bin/node
const cas = Math.floor(Number(process.argv[2]));
if (isNaN(cas)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < cas; i++) {
    console.log('C is fun');
  }
}
