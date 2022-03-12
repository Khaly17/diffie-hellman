""" ----------------------------------------------
Purpose : Implementation of Diffie-Hellman protocol
--------------------------------------------------- """

import random
import hashlib

# Mac/Linux: pip3 install pycryptodome
# Windows: py -m pip install pycryptodome
import Crypto.Util.number as cun
from Crypto.Cipher import AES

rand = random.SystemRandom()
#FLAG = b"buckeye{my_flag}"
# le b indique un tableau de byte et non un string
#M = b'MasterCCA1_UGB_2'
M = input("Enter votre message de 128 bits pour le chiffrement hybride\n").encode()
#M = ' '.join(format(c, 'b') for c in bytearray(m, "utf-8"))

def diffie_hellman(message: bytes):
    print("Original message : ", M)

    print("Parameter known by Alice and Bob")
    #Generate random prime p
    p = cun.getPrime(64)

    #Choose a generator  776488512
    g = 8
    print(f"p = {p}")
    print(f"g = {g}")

    print("***Alice***")
    #Alice / A
    xa = rand.randrange(2, p - 1)  # private key
    print("xa", xa)
    Y_a = pow(g, xa, p)  # public key
    # g ^ a === A  (mod p)
    print(f"xa = {xa}")
    print(f" Y_a = { Y_a}")


    # Bob
    print("***Bob***")
    xb = rand.randrange(2, p - 1)  # private key
    Y_b = pow(g, xb, p)  # public key
    print(f"xb = {xb}")
    print(f"Y_b = {Y_b}")
    # Y_b ^ xa === (g ^ xb) ^ xa === g ^ (xaxb)  (mod p)
    shared_secret_Y_a = pow(Y_b, xa, p)
    shared_secret_Y_b = pow(Y_a, xb, p)
    print("SharedKeyAlice", shared_secret_Y_a)
    print("SharedKeyBob", shared_secret_Y_b)

    # Use AES, a symmetric cipher, to encrypt the flag using the shared key
    #Encrypt message
    print("***Encrypt message by Alice***")
    key = hashlib.sha1(cun.long_to_bytes(shared_secret_Y_a)).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    ciphertext.hex()
    cipherFlag = ciphertext.hex()
    print(f"ciphertext = {cipherFlag}")

    #Decrypt message
    print("***Decrypt message***")
    key = hashlib.sha1(cun.long_to_bytes(shared_secret_Y_b)).digest()[:16]
    ciphertext = bytes.fromhex(cipherFlag)
    cipher = AES.new(key, AES.MODE_ECB)
    plain = cipher.decrypt(ciphertext)
#    print("flag", plain.decode('utf-8'))
    print(plain.decode('utf-8'))

print("Example of Diffe-Hellman implementation")
print()
diffie_hellman(M)
