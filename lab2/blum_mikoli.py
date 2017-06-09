import random

seed_length = 16
p = 97
g = 10


def blum_mikoli_generator(bitslength):
    global g, p
    seed = int(''.join(map(str, [random.choice([0, 1]) for _ in range(seed_length)])), 2)
    print('Seed {}'.format(seed))
    x = seed % p
    n = ''
    for i in range(bitslength):
        x = pow(g, x, p)
        n += str(int(bool(x < (p - 1) / 2)))
    return int(n, 2)
