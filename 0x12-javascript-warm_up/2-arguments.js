#!/usr/bin/node

const v = process.argv.length;
console.log(v === 2 ? 'No argument' : v === 3 ? 'Argument found' : 'Arguments found')
