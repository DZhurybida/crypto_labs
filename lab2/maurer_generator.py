import math
import random

from lab2.millerrabin import millerrabin
from prime import checkptab


def maurer_generator(k):
    global ptab
    RANDOM = random.SystemRandom()
    if k <= 20:
        while True:
            n = RANDOM.randint(2 ** (k - 1), 2 ** k - 1) | 1
            h = math.ceil(math.sqrt(n))
            for p in ptab[1:]:
                if p > h:
                    return (n)
                if (n % p) == 0:
                    break
    c = 0.005
    bb = math.ceil(c * k * k)
    checkptab(bb)
    m = 20
    if k > 2 * m:
        while True:
            s = RANDOM.uniform(0, 1)
            r = 2 ** (s - 1)
            if (k - r * k) > m:
                break
    else:
        r = 0.5
    q = maurer_generator(math.floor(r * k) + 1)
    ii = 2 ** (k - 1) // (2 * q)
    progress = True
    while progress:
        rr = RANDOM.randint(ii + 1, 2 * ii)
        n = 2 * rr * q + 1
        suc = 1
        for p in ptab:
            if p > bb:
                break
            if (n % p) == 0:
                suc = 0
                break
        if suc == 0:
            continue
        if millerrabin(n, 1) == 1:
            a = RANDOM.randint(2, n - 2)
            if pow(a, n - 1, n) == 1:
                b = pow(a, 2 * rr, n)
                if math.gcd(b - 1, n) == 1:
                    progress = False
    return n