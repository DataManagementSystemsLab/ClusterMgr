

To use nodejs

algorithm='sha1';
const secretEncoding = 'binary'
secret = Buffer.from([175, 254, 92, 155, 50, 241, 139, 149, 176, 180, 65, 45, 20, 222, 239, 119, 9, 57, 196, 157]);
let secretBuffer = Buffer.from(secret,secretEncoding);//Buffer.isBuffer(secret) ? secret : Buffer.from(secret, options.encoding);
const token_0 = hotp.createToken({secret:secretBuffer,counter:1, algorithm:'sha1'});
console.log(token_0);