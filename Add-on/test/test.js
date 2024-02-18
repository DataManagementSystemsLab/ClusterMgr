const otp = require('simpleotp');
const hotp = new otp.Hotp();
var speakeasy = require("speakeasy");
const crypto = require('crypto');

//const Hmotp = require('./hmotp'); // Importing MyClass from file1.js

// Create an instance of MyClass
//const hmotp = new Hmotp("John");
secret="V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5"
secret="testbase12345678"
// generate a token
const token_0 = hotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});

//const token1 = hmotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});

//print in node js
//console.log(token)
console.log(token_0)


const secretEncoding = 'binary'
const  secretLength = 20;

let secretBuffer = Buffer.from(secret,secretEncoding);//Buffer.isBuffer(secret) ? secret : Buffer.from(secret, options.encoding);

algorithm='sha1';
console.log(secretBuffer)
const  hash = crypto.createHmac(algorithm, secretBuffer);//.update(counter).digest();

console.log(hash);
var token = speakeasy.hotp({
    secret: secret.base32,
    encoding: 'base32',
    counter:0
  });
console.log(token)
