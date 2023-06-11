import matplotlib.pyplot as plt

import data
plt.hist(data.life_exp, bins=5)
plt.show()
plt.clf()

plt.hist(data.life_exp, bins=20)
plt.show()
plt.clf()
