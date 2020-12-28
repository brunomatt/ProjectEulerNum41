# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import time # This program takes about 2 seconds to run on my Lenovo Thinkpad -- Matthew Bruno 12/27/2020
start = time.time()

primes = []
pandigital_primes = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(7654321) # this program takes about 25 seconds to run if an 8 is placed in front, ie 87654321 and receives a SIGKILL if 987654321 is used.

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def pandigital_check(num):
    digits = deconstruct(num)
    limit = len(str(num))
    if sorted(digits) == [n for n in range(1,limit + 1)]:
        return True
    else:
        return False

for k in primes:
    if pandigital_check(k) is True:
        pandigital_primes.append(k)

answer = max(pandigital_primes)
print(answer)

stop = time.time()
print("Time: ", stop - start)