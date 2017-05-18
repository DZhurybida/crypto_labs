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
