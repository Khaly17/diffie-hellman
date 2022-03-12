import random
import hashlib

import Crypto.Util.numbers as cun 
from Crypto.Cipher import AES

rand =  random.SystemRandom()

m = input("Enter your message with 128 bits for your hybride chiffer").encode()

def deffie_hellman(message: bytes):
    print("Original message : ", m)

    p = cun.getPrime(128)

    g = 5

    print(f"p = {p}")
    print(f"g = {g}")

    print("***Alice***")

    xa = rand.randrange(2, p - 1) #private key
    print("xa", xa)

    Y_a = pow(g, xa, p) #public key
    
    print(f"xa = {xa}")
    print(f"Y_a = {Y_a}")


    print("***Bob***")

    xa = rand.randrange(2, p - 1) #private key
    print("xb", xb)

    Y_a = pow(g, xb, p) #public key
    
    print(f"xb = {xb}")
    print(f"Y_b = {Y_b}")

    shared_secret_Y_a = pow(Y_b, xa, p)
    shared_secret_Y_b = pow(Y_a, xb, p)

    print("sharedKeyAlice", shared_secret_Y_a)
    print("sharedKeyBob", shared_secret_Y_b)



deffie_hellman("Hello")