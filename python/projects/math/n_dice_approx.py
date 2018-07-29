
import random as rand
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

nb_of_launch = 10000
nb_dices = 10
dice_faces = 6
max_dice = nb_dices * 6

min_dice = nb_dices


proba_law = []
x = []
for i in range(max_dice):
    proba_law.append(0)
    x.append(i + 1)

for i in range(nb_of_launch):
    sum_dices = 0
    for j in range(nb_dices):
        dice = rand.randint(1,6)
        sum_dices += dice
    proba_law[sum_dices - 1] += 1

print(proba_law)

for i in range(len(proba_law)):
    proba_law[i] = proba_law[i] / nb_of_launch

# the histogram of the data

fig = plt.figure()


width = 0.5


plt.bar(x, proba_law, width, color='g')

plt.xlabel('Sum in output')
plt.ylabel('Probability')
plt.title('Probability law')
plt.show()