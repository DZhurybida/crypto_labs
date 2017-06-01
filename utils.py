import hashlib
import random

import math

import struct


def number_to_array(number):
    return list(map(int, str(number)))


def array_to_number(array):
    return int(''.join(map(str, array)))


def modinv(a, n):
    t, nt = 0, 1
    r, nr = n, a
    while nr != 0:
        q = r // nr
        t, nt = nt, t - q * nt
        r, nr = nr, r - q * nr
    if r > 1:
        return None
    while t < 0:
        t += n
    return t


def int_to_str(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big').decode("utf-8")


def int_from_str(string):
    return int.from_bytes(bytearray(string, 'utf-8'), 'big')


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


def text_to_hash(text):
    m = hashlib.md5()
    m.update(text)
    return int_from_bytes(m.digest())


def generator(p, a=None):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    while True:
        g = random.randint(2, p - 1)
        if a and g in a:
            continue
        if not (pow(g, (p - 1) // p1, p) == 1 or pow(g, (p - 1) // p2, p) == 1):
            return g


def prime_factors(n):
    nn = n
    factors = set()
    dvsr = 2
    dvsrSq = dvsr ** 2
    while dvsrSq <= nn:
        if n % dvsr == 0:
            factors.add(dvsr)
            while nn % dvsr == 0:
                nn //= dvsr
        dvsr += 1
        dvsrSq = dvsr ** 2
    if nn > 1:
        factors.add(nn)
    return factors


def is_generator(p, g):
    if math.gcd(p, g) == 0:
        return False
    p_minus_one = p - 1
    factors = prime_factors(p_minus_one)
    for f in factors:
        z = p_minus_one // f
        if pow(g, z, p) == 1:
            return False
    return True

def b(s):
    return s.encode("latin-1")


def long_to_bytes(n, blocksize=0):
    """long_to_bytes(n:long, blocksize:int) : string
    Convert a long integer to a byte string.
    If optional blocksize is given and greater than zero, pad the front of the
    byte string with binary zeros so that the length is a multiple of
    blocksize.
    """
    # after much testing, this algorithm was deemed to be the fastest
    s = b('')
    pack = struct.pack
    while n > 0:
        s = pack('>I', n & 0xffffffff) + s
        n = n >> 32
    # strip off leading zeros
    for i in range(len(s)):
        if s[i] != b('\000')[0]:
            break
    else:
        # only happens when n == 0
        s = b('\000')
        i = 0
    s = s[i:]
    # add back some pad bytes.  this could be done more efficiently w.r.t. the
    # de-padding being done above, but sigh...
    if blocksize > 0 and len(s) % blocksize:
        s += (blocksize - len(s) % blocksize) * b('\000')
    return s


def bytes_to_long(s):
    """bytes_to_long(string) : long
    Convert a byte string to a long integer.
    This is (essentially) the inverse of long_to_bytes().
    """
    acc = 0
    unpack = struct.unpack
    length = len(s)
    if length % 4:
        extra = (4 - length % 4)
        s = b('\000') * extra + s
        length += extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', s[i:i+4])[0]
    return acc
