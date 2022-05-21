
from cmath import sqrt
from math import floor

import time
import random

from matplotlib import pyplot as plt

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

primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]


Ns = []
Times = []
for i in range(0, 10000):

    ChosenP = random.choice(primes)
    ChosenQ = random.choice(primes)
    N = ChosenP * ChosenQ

    Time , p, q = BruteForceAttack(N)
    if (p == ChosenP and q == ChosenQ) or (p == ChosenQ and q == ChosenP):
        Ns.append(N)
        Times.append(Time)

# plotting the points 
plt.plot(Ns, Times)
  
# naming the x axis
plt.xlabel('N values')
# naming the y axis
plt.ylabel('Time taken')
  
# giving a title to my graph
plt.title('N vs Time for brute force attack')
  
# function to show the plot
plt.show()