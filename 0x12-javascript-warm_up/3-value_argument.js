#!/usr/bin/node
const cnt = process.argv[2];
if (cnt === undefined) {
	console.log('No argument');
} else {
	console.log(cnt);
}
