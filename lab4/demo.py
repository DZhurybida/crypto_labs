from lab4.elgamal import ElGamal
from utils import bytes_to_long, long_to_bytes

bit_length = 2048
# elgamal = ElGamal(bit_length)?
elgamal = ElGamal()
elgamal.save_config()
# m = maurer_generator(512)
m = b'Hello World'
m_number = bytes_to_long(m) + elgamal.p + elgamal.p
print(long_to_bytes(elgamal.decrypt(*elgamal.encrypt(m_number))))
