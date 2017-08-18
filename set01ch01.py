#!/usr/bin/python
from binascii import unhexlify, b2a_base64

inputvalue = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hexToBase64(string):
    result = string.decode('hex').encode('base64')

    if result.strip() == expected:
        return True
    else:
        return False

if hexToBase64(inputvalue) == True:
    print "Input matches expected value"
else:
    print "Input does not match expected value"
