//const otp = require('simpleotp');
//const hotp = new otp.Hotp();


const Hmotp = require('./hmotp'); // Importing MyClass from file1.js

// Create an instance of MyClass
const hmotp = new Hmotp("John");

// generate a token
//const token = hotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});

const token1 = hmotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});

//print in node js
//console.log(token)
console.log(token1)


