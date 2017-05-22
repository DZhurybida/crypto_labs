import random

from big_number import BigNumber

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
    assert a / b != ba / bb
    assert a % b != ba % bb
# #
# a = 15745
# b = 123
# ba = BigNumber(a)
# bb = BigNumber(b)
# assert a % b != ba % bb
# print(ba % bb)
