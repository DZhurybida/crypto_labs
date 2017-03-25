from copy import copy

from utils import array_to_number, number_to_array

BASE = 10


class BigNumber(object):

    def __init__(self, number, sign=1):
        if not isinstance(number, (list, tuple)):
            number = number_to_array(number)
        self.numbers = copy(number)
        self.sign = sign

    def add_zeros(self, amount):
        for i in range(amount):
            self.numbers.insert(0, 0)

    def multiply_by_ten(self, times):
        for i in range(times):
            self.numbers.append(0)
        return self

    def __add__(self, other):
        prepare(self, other)
        if self.sign == other.sign:
            return addition(self, other)
        else:
            if self.sign > 0:
                positive = self
                negative = other
            else:
                positive = other
                negative = self
            return subtraction(positive, negative)

    def __sub__(self, other):
        prepare(self, other)
        if self.sign != other.sign:
            return addition(self, other)
        else:
            return subtraction(self, other)

    def __ge__(self, other):
        for i in range(len(self)):
            if self[i] > other[i]:
                return True
            elif self[i] < other[i]:
                return False
        return True

    def __lt__(self, other):
        return not self >= other

    def __getitem__(self, item):
        return self.numbers[item]

    def __str__(self):
        number = array_to_number(self.numbers)
        return str(number * self.sign)

    def __len__(self):
        return len(self.numbers)

    def __neg__(self):
        self.sign *= -1
        return BigNumber(self.numbers, self.sign * -1)

    def __mul__(self, other):
        prepare(self, other)
        return BigNumber(karatsuba(self, other).numbers, self.sign * other.sign)


def prepare(u, v):
    len_u = len(u)
    len_v = len(v)
    if len_u != len_v:
        if len_u > len_v:
            v.add_zeros(len_u - len_v)
        else:
            u.add_zeros(len_v - len_u)


def addition(u, v):
    number_length = len(u)
    j = number_length - 1
    k = 0
    w = [0] * number_length
    while j >= 0:
        w[j] = (u[j] + v[j] + k) % BASE
        k = (u[j] + v[j] + k) // BASE
        j -= 1
    if k > 0:
        w.insert(0, k)
    return BigNumber(w, u.sign)


def subtraction(u, v):
    new_sign = u < v
    if new_sign:
        u, v = v, u
    number_length = len(u)
    j = number_length - 1
    k = 0
    w = [0] * number_length
    while j >= 0:
        w[j] = (u[j] - v[j] + k) % BASE
        k = (u[j] - v[j] + k) // BASE
        j -= 1
    return BigNumber(w, - u.sign if new_sign else u.sign)


def karatsuba(x, y):
    prepare(x, y)
    n = max(len(x), len(y))
    if n < 4:
        return BigNumber(
            number_to_array(
                array_to_number(x.numbers) * array_to_number(y.numbers)
            )
        )
    n_2 = n//2
    a, b = BigNumber(x[:-n_2]), BigNumber(x[-n_2:])
    c, d = BigNumber(y[:-n_2]), BigNumber(y[-n_2:])
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    p = karatsuba(a + b, c + d) - ac - bd
    return ac.multiply_by_ten((n_2)*2) + p.multiply_by_ten(n_2) + bd
