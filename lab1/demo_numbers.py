import random

from lab1.big_number import BigNumber

number_of_bits = 1024
num_of_tests = 100
for i in range(num_of_tests):
    a = random.getrandbits(number_of_bits)
    b = random.getrandbits(number_of_bits)
    ba = BigNumber(a)
    bb = BigNumber(b)
    if a < b:
        a, b = b, a
    assert a + b != ba + bb
    assert a - b != ba - bb
    assert a * b != ba * bb
