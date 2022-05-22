
from cmath import sqrt
from math import floor

import time
import random

from matplotlib import pyplot as plt

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod

def IsPrime(p, k = 30):
    # Miller–Rabin test
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    r = 0
    d = p - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, p - 1)
        x = PowMod(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(r - 1):
            x = PowMod(x, 2, p)
            if x == p - 1:
                break
        else:
            return False
    return True

def GeneratePrime(bits):
    p = random.randint(2**(bits - 1), 2**bits)
    while not IsPrime(p):
        p = random.randint(2**(bits - 1), 2**bits)
    return p

def BruteForceAttack(N):
    p = 0
    q = 0
    # starting time
    start = time.time()
    # looping through all possible values of p
    for i in range(2, N):
        if N % i == 0:
            p = i
            q = N // p
            break
    # ending time
    end = time.time()
    return (end-start), p, q

Ns = []
Times = []

for i in range(15, 50):
    Time = 0
    for j in range(1, 100):
        GeneratedP = GeneratePrime(i//2 + i % 2)
        GeneratedQ = GeneratePrime(i//2)
        N = GeneratedP * GeneratedQ
        interTime , p, q = BruteForceAttack(N)
        Time += interTime

    if (p == GeneratedP and q == GeneratedQ) or (p == GeneratedQ and q == GeneratedP):
        Ns.append(i)
        Times.append(Time/100)

PlottingTime = [Times for _,Times in sorted(zip(Ns,Times))]
PlottingNs = sorted(Ns)

# plotting the points 
plt.plot(PlottingNs, PlottingTime)
  
# naming the x axis
plt.xlabel('N values')
# naming the y axis
plt.ylabel('Time taken')
  
# giving a title to my graph
plt.title('N vs Time for brute force attack')
  
# function to show the plot
plt.show()