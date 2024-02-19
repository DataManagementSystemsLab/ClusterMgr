import pyotp
import hashlib
import base64
import hmac


def print_byte_array(r):
    s=""
    s+=('Byte Array (')
    s+= str(len(r))
    s+= ('):')
    for i in range(len(r)):
        b=r[i:i+1]
        s+=str(hex(int.from_bytes(b,'big')))
        s+=(' ' )
    s+=('\n')   
    print(s)
def byte_secret(secret) -> bytes:
        missing_padding = len(secret) % 8
        if missing_padding != 0:
            secret += "=" * (8 - missing_padding)
        return base64.b32decode(secret, casefold=False)
def int_to_bytestring(i: int, padding: int = 8) -> bytes:
        """
        Turns an integer to the OATH specified
        bytestring, which is fed to the HMAC
        along with the secret
        """
        result = bytearray()
        while i != 0:
            result.append(i & 0xFF)
            i >>= 8
        # It's necessary to convert the final result from bytearray to bytes
        # because the hmac functions in python 2.6 and 3.3 don't work with
        # bytearray
        return bytes(bytearray(reversed(result)).rjust(padding, b"\0"))        



input=0

k="V77FZGZS6GFZLMFUIEWRJXXPO4ETTRE5"
print_byte_array(byte_secret(k))
hasher = hmac.new(byte_secret(k), digestmod= hashlib.sha1)
hmac_hash = bytearray(hasher.digest())

print(hmac_hash)
print_byte_array(hmac_hash)

print("-----------")

hasher = hmac.new(byte_secret(k),int_to_bytestring(0), digestmod= hashlib.sha1)
hmac_hash = bytearray(hasher.digest())
print(hmac_hash)
print_byte_array(hmac_hash)


hotp = pyotp.HOTP(k)
print(hotp.at(1) )# => '260182'

#hotp = pyotp.HOTP('base32secret3232')
#hotp.at(0) # => '260182'
#print(hotp.at(0))


