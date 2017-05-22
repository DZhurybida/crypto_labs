from elgamal import ElGamal

elgamal = ElGamal()

elgamal.generate_keys()
print('Public keys: {}'.format(elgamal.public_key))
print('Private keys: {}'.format(elgamal.private_key))
# message = bytearray('Hello World', 'utf-8')
with open('weka-3-8-1-oracle-jvm.dmg', 'rb') as f:
    message = f.read()
a, b = elgamal.sign(message)

print('a: {}, b: {}'.format(a, b))
verified = elgamal.check_sign(message, a, b)
print('verified {}'.format(verified))
verified = elgamal.check_sign(message[::-1], a, b)
print('verified {}'.format(verified))
