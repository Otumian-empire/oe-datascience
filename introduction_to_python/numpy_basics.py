# introduction to numpy
# install numpy

# import numpy
import numpy as np

# numpy arrays
x = [1, 2, 3, 13]
x_np = np.array(x)

# print(x)
print(x_np)

# print(x*2)
# print(x_np*2)

# print(x_np + x_np)
# print(x_np * x_np)

# select all that are less 2
# operations
# print(x_np < 2)

# use as index, and print it out
# print(x_np[x_np < 2])
# print(x_np[:])
# print(x_np[1:3])

# xd_np = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ])

# print(xd_np)

# shape
print(x_np.shape)
# print(xd_np.shape)

# stack
# xs_np = np.column_stack((x_np, xd_np))
# print(xs_np)

# mean, median, std
# print(f"Mean is {np.mean(xd_np)}")
# print(f"Median is {np.median(xd_np)}")
mean = np.mean(x_np)
print(f"Mean is {mean}")

median = np.median(x_np)
print(f"Median is {median}")

# how far the data is spread out
# print(f"std is {round(np.std(xd_np), 3)}")
std = round(np.std(x_np), 3)
print(f"std is {std}")

# correlation
# print(f"correlation is {np.corrcoef(xd_np)}")
print(f"correlation is {np.corrcoef(x_np)}")


# simulate data with np.random.normal

print(np.random.normal(mean, std, 10))