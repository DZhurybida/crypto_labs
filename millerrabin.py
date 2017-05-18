import random


def millerrabin(n, t):
    if n <= 3:
        if n > 1:
            return True
        return False
    if n % 2 == 0:
        return False
    system_random = random.SystemRandom()
    d = n1 = n - 1
    r = 0
    while (d % 2) > 0:
        r += 1
        d //= 2
    r1 = r - 1
    for i in range(t):
        a = system_random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n1:
            continue
        j = 1
        while j <= r1 and x != n1:
            x = (x * x) % n
            if x == 1:
                return False
            j += 1

        if x != n1:
            return False
    return True
