import math
import random

from lab2.maurer_generator import maurer_generator
from lab2.millerrabin import millerrabin
from utils import modinv, generator

FILEPATH = 'key.txt'


def is_generator(p, q, g):
    if pow(g, 2, q) == 1:
        return False
    if pow(g, p, q) == 1:
        return False
    return True


def get_prime_and_generator(key_length):
    while True:
        p = maurer_generator(key_length - 1)
        q = p * 2 + 1
        if millerrabin(q, 1):
            break
    print(p)
    print(q)
    a = set()
    while True:
        g = generator(q, a)
        a.add(g)
        print(g)
        if is_generator(p, q, g):
            break
    return q, g

class ElGamal(object):
    def __init__(self, bit_length=None):
        if not bit_length:
            with open(FILEPATH, 'r') as f:
                self.p = int(f.readline(), 16)
                self.g = int(f.readline(), 16)
                self.a = int(f.readline(), 16)
                self.r = int(f.readline(), 16)
        else:
            self.p, self.g = get_prime_and_generator(bit_length)
            self.a = random.randint(1, self.p - 1)
            self.r = pow(self.g, self.a, self.p)

    def save_config(self):
        with open(FILEPATH, 'w') as f:
            f.write(hex(self.p))
            f.write('\n')
            f.write(hex(self.g))
            f.write('\n')
            f.write(hex(self.a))
            f.write('\n')
            f.write(hex(self.r))

    def _get_k(self):
        while True:
            k = random.randint(1, self.p - 1)
            if math.gcd(k, self.p - 1) == 1:
                return k

    def encrypt(self, m):
        m %= self.p
        k = self._get_k()
        return pow(self.g, k, self.p), pow(self.r, k, self.p) * m % self.p

    def decrypt(self, a, b):
        c = modinv(pow(a, self.a, self.p), self.p)
        return c * b % self.p
