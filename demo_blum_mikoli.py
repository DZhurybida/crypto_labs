import time

from blum_mikoli import blum_mikoli_generator
from millerrabin import millerrabin

nb = 1024
while True:
    start = time.clock()
    n = blum_mikoli_generator(nb)
    print("Prime generation time %6.3f sec" % (time.clock() - start))
    print('Number {}'.format(n))
    print('Number length {}'.format(len(str(n))))
    is_prime = millerrabin(n, 1)
    print('is prime {}'.format(is_prime))
    if is_prime:
        break

print("Prime generation time %6.3f sec" % (time.clock() - start))
print('Number {}'.format(n))
print('Number length {}'.format(len(str(n))))
is_prime = millerrabin(n, 1)
print('is prime {}'.format(is_prime))
n1 = int(n)
print('Bit length {}'.format(n1.bit_length()))
