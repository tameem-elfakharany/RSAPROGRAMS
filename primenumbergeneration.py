import math
import random

def primenum(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    else:
        bound = math.sqrt(n) + 1
        for i in range(3, int(bound), 2):
            if n % i == 0:
                return False
        return True

def randomprimenum(bit_length):
    while True:
        number = random.getrandbits(bit_length)
        if number % 2 != 0 and primenum(number):
            return number

# #bit_length = int(input("Enter the bit length: "))
p=randomprimenum(16)
q=randomprimenum(16)
# n=p*q
# eul_phi=(p-1)*(q-1)
# e=65537
# def extended_GCD(a, b):
#     x0, x1, y0, y1 = 1, 0, 0, 1
#     while b:
#         q, a, b = a // b, b, a % b
#         x0, x1 = x1, x0 - q * x1
#         y0, y1 = y1, y0 - q * y1
#     return a, x0, y0

# # Find a suitable e that is coprime with phi(n)
# while True:
#     gcd, _, _ = extended_GCD(e, eul_phi)
#     if gcd == 1:
#         break
#     else:
#         e += 1

# #getting d and ensuring its positive
# gcd, d, _ = extended_GCD(e, eul_phi)

# def ensure_positive_d(d, phi_n):
#     """Ensure that the private exponent d is positive."""
#     while d < 0:
#         d += phi_n
#     return d

# d = ensure_positive_d(d, eul_phi)
# message= 11
# C = pow(message, e, n)
# M = pow(C, d, n)
# publickey = (n, e)
# privatekey = (n, d)
print("p is: ", p,"\nq is: ",q)
# print("d is: ", d, "n is: ",n)
# print("Public Key : ", publickey, "\nPrivate Key :", privatekey)
# print("Encrypted Message : ", C, "\nDecrypted Message : ", M)