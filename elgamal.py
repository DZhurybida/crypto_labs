import math
import random


from maurer_generator import maurer_generator
from utils import int_from_bytes, modinv, text_to_hash

key_length = 2048


class ElGamal(object):
    public_key = None
    private_key = None

    def __int__(self, public_key=None, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    def generate_keys(self):
        p = maurer_generator(key_length)
        g = random.randint(1, p - 1)
        x = random.randint(1, p - 1)
        y = pow(g, x, p)
        self.public_key = (y, g, p)
        self.private_key = x

    def _get_k(self):
        p = self.public_key[2]
        while True:
            k = random.randint(1, p - 1)
            if math.gcd(k, p - 1) == 1:
                return k

    def sign(self, message):
        m = text_to_hash(message)
        y, g, p = self.public_key
        x = self.private_key
        k = self._get_k()
        a = pow(g, k, p)
        inv_k = modinv(k, p - 1)
        b = (m - x * a) * inv_k % (p - 1)
        return a, b

    def check_sign(self, message, a, b):
        m = text_to_hash(message)
        y, g, p = self.public_key
        # return (y ** a * a ** b) % p == pow(g, m, p)
        # return (y ** a * a ** b) % p == pow(g, m, p)
        # return (pow(y, a) * pow(a, b)) % p == pow(g, m, p)
        return (pow(y, a, p) * pow(a, b, p)) % p == pow(g, m, p)


def exp_by_squaring_iterative(x, n):
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x = x * x
            n = n / 2
        else:
            y = x * y
            x = x * x
            n = (n - 1) / 2
    print('X: {}, Y: {}'.format(x, y))
    return x * y
