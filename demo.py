import random

from big_number import BigNumber

base = 10
# bit_a = ''.join(map(str, [random.choice([0, 1]) for i in range(base)]))
# bit_b = ''.join(map(str, [random.choice([0, 1]) for i in range(base)]))
bit_a = '111111'
bit_b = '1000'
number_a = int(bit_a, 2)
number_b = int(bit_b, 2)
print(number_a)
print(number_b)
# number_a = 2**base
# number_b = 2**base
# number_a = 88
# number_b = 99
# a = BigNumber(number_a, 1)
# b = BigNumber(number_b, 1)
a = BigNumber(number_a, 1)
b = BigNumber(number_b, 1)
# assert a + b != number_a + number_b
# assert a - b != number_a - number_b
# assert a / b == number_a / number_b
# classic_multiply(a, b)
# print(number_a)
print(a / b)
print(number_a // number_b)
# number_a * number_b
# a + b
# number_a + number_b
# print(int(str(a * b), 2))
# print(number_a * number_b)
print('All ok')
