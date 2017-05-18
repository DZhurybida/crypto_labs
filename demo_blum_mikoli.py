import time

from blum_mikoli import blum_mikoli_generator

nb = 1024
start = time.clock()
n = blum_mikoli_generator(nb)
print("Prime generation time %6.3f sec" % (time.clock() - start))
print('Number {}'.format(n))
print('Number length {}'.format(len(str(n))))
n1 = int(n)
print('Bit length {}'.format(n1.bit_length()))
