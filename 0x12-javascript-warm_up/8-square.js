#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < num; i++) {
    let rw = '';
    for (let s = 0; s <num; ++s) row += 'X';
    console.log(rw);
  }
}
