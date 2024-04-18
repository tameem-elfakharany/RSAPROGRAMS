import math
from primenumbergeneration import randomprimenum

p = randomprimenum(8)
q = randomprimenum(8)
while p==q:
    q=randomprimenum(8)

n = p * q
eul_phi = (p - 1) * (q - 1)

def extended_GCD(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Find a suitable e that is coprime with phi(n)
e = 3
while True:
    gcd, _, _ = extended_GCD(e, eul_phi)
    if gcd == 1:
        break
    else:
        e += 1

gcd, d, _ = extended_GCD(e, eul_phi)

def prime_factorization(n):
    """Factorize a prime number into its prime factors."""
    factors = []
    for divisor in range(2, int(n**0.5) + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    if n > 1:
        factors.append(n)
    return factors

# Use tuples to represent keys
publickey = (n, e)
privatekey = (n, d)

print("Public Key : ", publickey, "\nPrivate Key :", privatekey)
print("p is: ", p, "\nq is: ",q)

#factorise n to obtain p and q 
factors=prime_factorization(n)
factorisedp=factors[1]
factorisedq=factors[0]

message= 112
C = pow(message, e, n)
M = pow(C, d, n)
print("Encrypted Message : ", C, "\nDecrypted Message : ", M)
print(f"factorised p and q from modulus of n are: {factorisedp},{factorisedq}")









