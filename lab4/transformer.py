# def twoscomplement_to_unsigned(i):
#     return i % 256
#
# bytes(map(twoscomplement_to_unsigned, b))
import binascii
from io import StringIO


def unpad(text, blkSz):
    '''
    Remove the PKCS#7 padding from a text string
    '''
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val > blkSz:
        raise ValueError('Input is not padded or padding is corrupt')

    l = nl - val
    return text[:l]


def pad(text, blkSz):
    '''
    Pad an input string according to PKCS#7
    '''
    l = len(text)
    output = StringIO()
    val = blkSz - (l % blkSz)
    for _ in range(val):
        output.write('%02x' % val)
    return text + binascii.unhexlify(output.getvalue())

