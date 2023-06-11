# customizations
# different types of plots
# ~ on data and information to convey

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

# plot: x-axis and y-axis
plt.plot(year, population)

# labels: xlabel and ylabel
plt.xlabel("Year")
plt.ylabel("Population")

# title for the plot
plt.title("World population project")

# ticks: indicates where the data set starts on the plot
plt.xticks([1945, 1965, 1985, 2015], ['45"', '65"', '85"', '2k"'])
plt.yticks([2, 4, 6, 8], ['2B', '4B', '6B', '8B'])
# show plot
plt.show()
