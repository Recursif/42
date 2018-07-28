
import random as rand
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

nb_of_launch = 10000
nb_dices = 2
dice_faces = 6
max_dice = nb_dices * 6

min_dice = nb_dices


density = []
x = []
for i in range(max_dice):
    density.append(0)
    x.append(i)

for i in range(nb_of_launch):
    sum_dices = 0
    for j in range(nb_dices):
        dice = rand.randint(1,6)
        sum_dices += dice
    density[sum_dices - 1] += 1

print(density)

for i in range(len(density)):
    density[i] = density[i] / nb_of_launch

# the histogram of the data

fig = plt.figure()


width = 1


plt.bar(x, density, width, color='g')

plt.show()