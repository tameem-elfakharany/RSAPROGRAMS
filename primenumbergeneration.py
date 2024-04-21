import math
import random

#ensuring number is prime
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

#generating random prime based on bit length
def randomprimenum(bit_length):
    while True:
        number = random.getrandbits(bit_length)
        if number % 2 != 0 and primenum(number):
            return number


p=randomprimenum(8)
q=randomprimenum(8)
