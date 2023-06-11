import matplotlib.pyplot as plt
from data import life_exp, gdp_cap

# plt.plot(gdp_cap, life_exp)
# when you're trying to assess if there's a correlation between
# two variables, for example, the scatter plot is the better
# choice. Below is an example of how to build a scatter plot.
plt.scatter(gdp_cap, life_exp)

# A correlation will become clear when you display the GDP
# per capita on a logarithmic scale. Add the line plt.xscale('log')
plt.xscale("log")
plt.show()
