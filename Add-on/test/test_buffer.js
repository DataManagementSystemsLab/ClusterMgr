const base32 = require('base32');
var atob = require('atob');
// Encode a string in base64
function base64ToArrayBuffer(base64) {
    var binaryString = atob(base64);
    var bytes = new Uint8Array(binaryString.length);
    for (var i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
    }
    return bytes.buffer;
}

const base64String = 'V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5';
//const buffer = Buffer.from(base64String, 'base64');
//const bytearray = buffer.toString('binary');

// Decode the base64 string to base32

// Print the base32 string
console.log(base64ToArrayBuffer(base64String));


//conver t

function byteSecret(secret) {
    // Calculate missing padding
    const missingPadding = (secret.length % 8) || 0;
  
    // Pad if necessary
    if (missingPadding) {
      secret += '='.repeat(8 - missingPadding);
    }
  
    // Decode base32 using Buffer
    return Buffer.from(secret, 'base64');
  }
  
  // Example usage
  const secret = "00000000";
  const bytes = byteSecret(secret);
  console.log(bytes);