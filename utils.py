import hashlib


def number_to_array(number):
    return list(map(int, str(number)))


def array_to_number(array):
    return int(''.join(map(str, array)))


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


def int_to_str(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big').decode("utf-8")


def int_from_str(string):
    return int.from_bytes(bytearray(string, 'utf-8'), 'big')


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


def text_to_hash(text):
    m = hashlib.md5()
    m.update(text)
    return int_from_bytes(m.digest())
