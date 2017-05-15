import random

from prime import millerrabin

p = 97
g = 10
base = 16
seed = int(''.join(map(str, [random.choice([0, 1]) for i in range(base)])), 2)


def cal_pow(pow, val):
    if pow == 0:
        return 1
    v = cal_pow(pow/2, val)
    if pow % 2 == 0:
        return (v*v) % p
    else:
        return (((v*val) % p) * v) % p


def get_prime():
    global g, p, base, seed
    x = cal_pow(seed, g)
    if x % p < (p - 1) / 2:
        n = '1'
    else:
        n = '0'
    for i in range(base):
        tmp = (cal_pow(int(n[-1]), n)) % p
        x += tmp
        n += str(int(bool(x < (p - 1) / 2)))
    return n

n = get_prime()
print("number %s " % n)
print("isprime %s " % millerrabin(n, 1, 1))
