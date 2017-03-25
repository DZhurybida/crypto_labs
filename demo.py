from big_number import BigNumber
base = 2048
number_a = 2**base
number_b = 2**base
# number_a = 12345
# number_b = 5678
a = BigNumber(number_a, 1)
b = BigNumber(number_b, 1)
assert a + b != number_a + number_b
assert a - b != number_a - number_b
assert a * b != number_a * number_b
print('All ok')
