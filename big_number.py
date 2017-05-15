from copy import copy
from array import array

from utils import array_to_number, number_to_array

BASE = 10


class BigNumber(object):

    def __init__(self, number, sign=1):
        if not isinstance(number, (list, tuple, array)):
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

    def truncate_zeros(self):
        counter = 0
        for i in range(len(self)):
            if self[i] == 0:
                counter += 1
            else:
                break
        else:
            return BigNumber(self[:-counter])
        return BigNumber(self.numbers)

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

    def __isub__(self, other):
        return self - other

    def __ge__(self, other):
        prepare(self, other)
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

    def __truediv__(self, other):
        # prepare(self, other)
        q, r = division(self, other)
        return q

    def __divmod__(self, other):
        # prepare(self, other)
        q, r = division(self, other)
        return r


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


def classic_multiply(u, v):
    u = BigNumber(list(reversed(u.numbers)), u.sign)
    v = BigNumber(list(reversed(v.numbers)), v.sign)
    product = [0] * (len(u) + len(v))
    for b_i in range(len(v)):
        carry = 0
        for a_i in range(len(v)):
            product[a_i + b_i] += carry + u[a_i] * v[b_i]
            carry = product[a_i + b_i] // BASE
            product[a_i + b_i] %= BASE
        product[b_i + len(u)] += carry
    return BigNumber(list(reversed(product)), u.sign * v.sign)


def karatsuba(x, y):
    prepare(x, y)
    n = max(len(x), len(y))
    if n < 100:
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
    return ac.multiply_by_ten(n_2 * 2) + p.multiply_by_ten(n_2) + bd


def division(n, d):
    n = n.truncate_zeros()
    d = d.truncate_zeros()
    if d.sign < 0:
        q, r = division(n, BigNumber(d.numbers, -1 * d.sign))
        return q * -1, r
    if n.sign < 0:
        q, r = division(n, -1 * n)
        if r < 0:
            return -1 * q, r
        else:
            q = BigNumber(q.numbers, q.sign * -1) - BigNumber(1)
            r = d - r
            return q, r
    q = BigNumber(0)
    r = n
    while r > d:
        q = q + BigNumber(1)
        r = r - d
    return q, r
