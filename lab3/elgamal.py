import math
import random

from lab2.maurer_generator import maurer_generator
from utils import modinv, text_to_hash, generator

key_length = 512



class ElGamal(object):
    public_key = None
    private_key = None

    def __int__(self, public_key=None, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    def generate_keys(self):
        p = maurer_generator(key_length)
        g = generator(p)
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
        return (pow(y, a, p) * pow(a, b, p)) % p == pow(g, m, p)
