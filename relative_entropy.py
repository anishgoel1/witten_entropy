import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def relative_entropy(p_dist, q_dist):
    """
    :param p_dist: probability distribution == p
    :param q_dist: probability distribution == q
    :return: relative entropy // KL == D_{KL}(P || Q)
    """
    return sum([p * math.log2(p / q) for p, q in zip(p_dist, q_dist)])


data = np.arange(-3, 3, 0.001)
dist_p = norm.pdf(data, 0, 1)
dist_q = norm.pdf(data, 0, 1.1)

plt.plot(data, dist_p, linewidth=2.5, label='P: μ=0, σ=1', color='green')
plt.plot(data, dist_q, linewidth=2.5, label='Q: μ=0, σ=1.1', color='red')
plt.fill_between(data, dist_p, dist_q, color='gold', alpha=0.3)
plt.text(-3.2, 0.405, f'RELATIVE ENTROPY: {relative_entropy(dist_p, dist_q):.2f}', weight='bold')
plt.ylim(0, 0.425)
plt.legend()
plt.show()
