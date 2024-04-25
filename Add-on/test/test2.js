const otp = require('simpleotp');
const hotp = new otp.Hotp();
//var speakeasy = require("speakeasy");

//const Hmotp = require('./hmotp'); // Importing MyClass from file1.js

//const hmotp = new Hmotp("John");
// generate a token
const token_0 = hotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});
//const token1 = hmotp.createToken({secret:'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5',counter:0, algorithm:'sha1'});

const crypto = require('crypto');

var secret="V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5"
algorithm='sha1';

//const buffer = Buffer.from(base64ToBase32(secret), 'base32');
//console.log(buffer)
const secretEncoding = 'binary'
secret = Buffer.from([175, 254, 92, 155, 50, 241, 139, 149, 176, 180, 65, 45, 20, 222, 239, 119, 9, 57, 196, 157]);
let secretBuffer = Buffer.from(secret,secretEncoding);//Buffer.isBuffer(secret) ? secret : Buffer.from(secret, options.encoding);
console.log(secretBuffer)
const  hash = crypto.createHmac(algorithm, secretBuffer);//.update(counter).digest();
console.log(hash.digest());
console.log("-----------")
const counter = Buffer.from([0, 0, 0, 0, 0, 0, 0, 0]);
const  hash0 = crypto.createHmac(algorithm, secretBuffer).update(counter);//.digest();
console.log(hash0.digest());

/*var token = speakeasy.hotp({
    secret: secret.base32,
    encoding: 'base32',
    counter:0
  });
console.log(token)
*/

const base32 = require('base32');

// Encode a string in base64
const base64String = 'SGVsbG8gV29ybGQh';

// Decode the base64 string to base32
const base32String = base32.decode(base64String);

// Print the base32 string
console.log(base32String);