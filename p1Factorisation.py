import math
import time
from primenumbergeneration import randomprimenum




#p and q random number generation
# p = randomprimenum(16)
# q = randomprimenum(16)
p=223
q=47


# while p==q:
#     """making sure they're not equal"""
#     q=randomprimenum(16)

#start time 
starttime=time.time()
#calculations
n = p * q
eul_phi = (p - 1) * (q - 1)

#Extended GCD
def extended_GCD(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Find a suitable e that is coprime with phi(n)
e = 365537
while True:
    gcd, _, _ = extended_GCD(e, eul_phi)
    if gcd == 1:
        break
    else:
        e += 1

#getting d and ensuring its positive
gcd, d, _ = extended_GCD(e, eul_phi)

def ensure_positive_d(d, phi_n):
    """Ensure that the private exponent d is positive."""
    while d < 0:
        d += phi_n
    return d

d = ensure_positive_d(d, eul_phi)

factors = []
def prime_factorization(n):
    """Factorize a prime number into its prime factors."""
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

#obtaining p and q from n by factorisation
factors=prime_factorization(n)
p_factorised_from_n=factors[1]
q_factorised_from_n=factors[0]

#calculating time
endtime=time.time()
time=(endtime-starttime) *1000

#message encryption (C) and decryption (M)
message= 11
C = pow(message, e, n)
M = pow(C, d, n)

#printing keys and generated p and q 
print("factorisation result is: ")
print("Public Key : ", publickey, "\nPrivate Key :", privatekey)
print("p is: ", p, "\nq is: ",q)

#printing encryption and decryption and factorised values
print("Encrypted Message : ", C, "\nDecrypted Message : ", M)
print(f"factorised p and q from modulus of n are: {p_factorised_from_n},{q_factorised_from_n}")

# printing time
print("time in milliseconds is: ", time)










