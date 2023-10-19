const fs = require('fs');

const json = fs.readFileSync(__dirname + '/' + 'index.json').toString();

const object = JSON.parse(json);
const nameObject = JSON.parse(object.name);

console.log('json', json, typeof json);
console.log('object', object, typeof object);
console.log('nameObject', nameObject, typeof nameObject);
