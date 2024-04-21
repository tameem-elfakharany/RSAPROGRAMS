import math
import time 
from primenumbergeneration import randomprimenum



#p and q random number generation
p = randomprimenum(8)
q = randomprimenum(8)

while p==q:
    """making sure they're not equal"""
    q=randomprimenum(8)


#start time 
starttime=time.time()

#calculations
n = p * q
eul_phi = (p - 1) * (q - 1)
e = 65537

#encrypting
message= 11
C = pow(message, e, n)

#finding d using brute force
def brute_force_decryption(C,n,e):
    attempts=0
    d=1
    while True:
        M=pow(C,d,n)
        if M==message:
            break
        d+=1
        attempts+=1
    return d, attempts

d,attempts=brute_force_decryption(C,n,e)

def ensure_positive_d(d, phi_n):
    """Ensure that the private exponent d is positive."""
    while d < 0:
        d += phi_n
    return d

d = ensure_positive_d(d, eul_phi)
M=pow(C,d,n)

# Use tuples to represent keys
publickey = (n, e)
privatekey = (n, d)

#calculating time
endtime=time.time()
time=(endtime-starttime)*1000

print("Brute force: ")
print("d (private exponent) is: ", d)
print("Number of attempts is: ", attempts)
print("Public Key : ", publickey, "\nPrivate Key :", privatekey)
print("P is: ", p, "\nq is: ",q)
print("n is: ", n, "\ne is: ", e, "\neuler: ", eul_phi)
print("time taken in milliseconds is: ", time)
print("Encrypted Message : ", C, "\nDecrypted Message : ", M)