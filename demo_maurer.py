import time

from prime import provableprime

nb = 1000
start = time.clock()
n = provableprime(nb)
print("Prime generation time %6.3f sec" % (time.clock() - start))
print(n)
