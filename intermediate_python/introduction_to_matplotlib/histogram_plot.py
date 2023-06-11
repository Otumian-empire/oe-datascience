import matplotlib.pyplot as plt

from data.life_exp import life_exp


plt.hist(life_exp, bins=5)
plt.show()
plt.clf()

plt.hist(life_exp, bins=20)
plt.show()
plt.clf()
