def number_to_array(number):
    return list(map(int, str(number)))


def array_to_number(array):
    return int(''.join(map(str, array)))
