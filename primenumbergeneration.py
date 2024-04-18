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

#bit_length = int(input("Enter the bit length: "))
bit_length=8
randomprime = randomprimenum(bit_length)
print("random prime of bit length ",bit_length, "is: ", randomprime)
