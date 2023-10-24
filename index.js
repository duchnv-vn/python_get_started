const fs = require('fs');

// const json = fs.readFileSync(__dirname + '/' + 'index.json').toString();

// const object = JSON.parse(json);
// const nameObject = JSON.parse(object.name);

// console.log('json', json, typeof json);
// console.log('object', object, typeof object);
// console.log('nameObject', nameObject, typeof nameObject);

// -----------------------------------------------------------------------------
let [a, b] = [1, 2];

[b, a] = [a, b];

// console.log('a', a);
// console.log('b', b);

[c, d] = '12';
c = '3';

console.log('c', c);
console.log('d', d);
