#!/usr/bin/python

import array
import binascii
import operator

from itertools import imap


def bytes_xor(a, b):
    aa = array.array('B', a)
    bb = array.array('B', b)

    return array.array('B', imap(operator.xor, aa, bb)).tostring()


inputString = u'1c0111001f010100061a024b53535009181c'
xorString = u'686974207468652062756c6c277320657965'
expectedResult = u'746865206b696420646f6e277420706c6179'

hexInput = binascii.unhexlify(inputString)
hexXor = binascii.unhexlify(xorString)

result = bytes_xor(hexInput,hexXor)
result = binascii.hexlify(result).decode('ascii')

print("Result: {}".format(result))
print("Success: {}".format(result == expectedResult))
