from math import gcd
import math, random, time


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


ptab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def checkptab(trialdivbound):
    global ptab
    g = ptab[-1]
    while ptab[-1] < trialdivbound:
        g += 2
        h = math.ceil(math.sqrt(g))
        for p in ptab:
            if p > h:
                suc = 1
                break
            if (g % p) == 0:
                suc = 0
                break
        if suc == 0:
            continue
        ptab += [g]
    return


checkptab(2 ** 10)


def millerrabin(n, t, kn):
    assert t >= 1 and 0 <= kn <= 1
    if n <= 3:
        if n > 1:
            return 1
        return 0
    elif n % 2 == 0:
        return 0
    RANDOM = random.SystemRandom()
    r = n1 = n - 1
    s = 0
    while (r % 2) > 0:
        s += 1
        r //= 2
    s1 = s - 1
    for i in range(t):
        if i == 0 and kn == 1:
            a = 2
        else:
            a = RANDOM.randint(2, n - 2)
        y = pow(a, r, n)
        if y != 1 and y != n1:
            j = 1
            while j <= s1 and y != n1:
                y = (y * y) % n
                if y == 1:
                    return 0
                j += 1
            if y != n1:
                return 0
    return 1


def provableprime(k):
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
    q = provableprime(math.floor(r * k) + 1)
    ii = 2 ** (k - 1) // (2 * q)
    success = 0
    while success == 0:
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
        if millerrabin(n, 1, 1) == 1:
            a = RANDOM.randint(2, n - 2)
            if pow(a, n - 1, n) == 1:
                b = pow(a, 2 * rr, n)
                if gcd(b - 1, n) == 1:
                    success = 1
    return n
