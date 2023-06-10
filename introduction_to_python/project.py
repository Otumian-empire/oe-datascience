# this is a simple project to demonstrate all that
# I have learnt from the numpy course
# import numpy
import matplotlib.pyplot as plt
import numpy as np

# create a random data set with a mean, std, size
# mean: 4.5, std: 12.5, size: 100
# data_set = np.random.normal(4.5,  12.5, 100)
data_set = np.random.normal(10,  10, 1000)


# print the data set
print(data_set)

# convert the data set to a numpy array
np_data_set = np.array(data_set)

# print the type and shape of the numpy array
print(type(np_data_set))
print(np_data_set.shape)


# find the mean, median and std
mean = np.mean(np_data_set)
median = np.median(np_data_set)
std = np.std(np_data_set)

# print the mean, median and std
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Std: {std}")


# use clip to get a different view of the data set
clip_data_set = np.clip(np_data_set, mean - std, mean+std)
print(clip_data_set)

# find the mean, median and std of the clipped data set
clip_mean = np.mean(clip_data_set)
clip_median = np.median(clip_data_set)
clip_std = np.std(clip_data_set)

# print the mean, median and std
print(f"Mean: {clip_mean}")
print(f"Median: {clip_median}")
print(f"Std: {clip_std}")


plt.plot(np_data_set, "k.")
plt.axhline(y=mean,       color='red', linestyle='-', label='Mean')
plt.axhline(y=mean + std, color='orange', linestyle='--', label='Mean + Std')
plt.axhline(y=mean - std, color='yellow', linestyle='--', label='Mean - Std')
plt.axhline(y=mean + 2*std, color='orange',
            linestyle='--', label='Mean + 2Std')
plt.axhline(y=mean - 2*std, color='yellow',
            linestyle='--', label='Mean - 2Std')

plt.axhline(y=clip_mean,       color="green",
            linestyle='-', label='clipped Mean')
plt.axhline(y=clip_mean + clip_std, color='blue',
            linestyle='--', label='clipped Mean + Std')
plt.axhline(y=clip_mean - clip_std, color='indigo',
            linestyle='--', label='clipped Mean - Std')

plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Data Plot with Mean and Standard Deviation')
plt.legend()

plt.show()
