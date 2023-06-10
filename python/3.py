#!/usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class
from Random import Random

results = []
for n in range(99):
    results.append(Random.Categorical(0.5))

plt.hist(results, 50, density=True, facecolor='g', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Categorical random number generator')
plt.grid(True)

# show figure (program only ends once closed)
plt.show()
