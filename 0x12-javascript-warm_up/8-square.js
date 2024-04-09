#!/usr/bin/node
const r = process.argv[2];
if (isNaN(r)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < r; i++) {
    console.log('X'.repeat(r));
  }
}
