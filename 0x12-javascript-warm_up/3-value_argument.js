#!/usr/bin/node

let args = false;

for (let x = 2; process.argv(x) !== undefined; x++){
	args = true;
	break;
}
if (args) {
	const argsFirst = process.argv.slice(2);
}else {
	console.log("No argument")
}
