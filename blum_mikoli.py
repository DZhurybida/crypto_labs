from big_number import BigNumber, ONE, ZERO, TWO

p = BigNumber(97)
g = BigNumber(10)
seed_length = 16
# seed = BigNumber(int(''.join(map(str, [random.choice([0, 1]) for i in range(seed_length)])), 2))
seed = BigNumber(28086)
print('Seed {}'.format(seed))


def blum_mikoli_generator(bitslength):
    global g, p, seed
    x = seed % p
    n = ''
    for i in range(bitslength):
        x = optimal_pow(g, x, p)
        n += str(int(bool(x < (p - ONE) / TWO)))
    return int(n, 2)


def optimal_pow(base, exponent, modulus):
    if modulus == ONE:
        return ZERO
    result = ONE
    base %= modulus
    while exponent > ZERO:
        if exponent % TWO == ONE:
           result = (result * base) % modulus
        exponent = exponent / TWO
        base = (base * base) % modulus
    return result
