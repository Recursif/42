
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


# the histogram of the data

fig = plt.figure()


width = 0.5


plt.bar(x, proba_law, width, color='g')

plt.xlabel('Sum in output')
plt.ylabel('Probability')
plt.title('Probability law')
plt.show()