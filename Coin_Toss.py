import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

n = 1 
p = 0.5

# Different numbers of trials
trials = [2, 5, 10, 20, 50, 100]




for n in trials:
    # Plotting
    plt.figure(figsize=(12, 8))
    x = np.arange(0, n + 1)
    binom_dist = binom.pmf(x, n, p)
    plt.plot(x, binom_dist, 'o-', label=f'n = {n}')
    plt.title(f'Probability Distribution when {n} coins are tossed')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid()
    plt.show()