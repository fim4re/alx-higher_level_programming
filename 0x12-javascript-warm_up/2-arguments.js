#!/usr/bin/node

const cnt = process.argv.length;

if (cnt === 2) {
	console.log('No argument');
} else if (cnt === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
