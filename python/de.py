import random as rand
from math import sqrt

total = 10000
nbsix = 0
de = rand.randint(1,6)
n = 0
while n < total:
    de = rand.randint(1,6)
    if (de == 6):
        nbsix += 1
    n += 1

print(nbsix/total)
print(1/6)
print(sqrt( (nbsix/total- 1/6)**2) * 100)
