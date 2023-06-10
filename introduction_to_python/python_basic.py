# this is comment

# this is a print statement
print("Hello world")

# type of data
print(type(1))
print(type(1.0))
print(type("Python Basics"))


# multiplication, exponentiation, division, modulo,
# addition, subtraction, parenthesis
print(2 * 4)
print(2 ** 4)
print(2 / 4)
print(2 // 4)  # floor division
print(2 % 4)
print(2 + 4)
print(2 - 4)
print((2**((2 - 4) + (2 // 4))))


# variable
course_code = "DCIT 316"
print(course_code)
print(type(course_code))

unit_cost_price = 4000  # the cost of one product
unit_selling_price = 5000  # the cost of one product
product_count = 10000  # the number of products available

expenses = product_count * unit_cost_price
revenue = product_count * unit_selling_price

profit = revenue - expenses

print(f"No. Products: {product_count}")
print(f"Unit cost price: ${unit_cost_price}")
print(f"Unit selling price: ${unit_selling_price}")
print(f"Product cost: ${expenses}")
print(f"Revenue generated: ${revenue}")
print(f"Profit made: ${profit}")

# Data types: int, str, bool, float
print("Repeat " * 3)
print("Repeat " + str(3))

# String indexing
sample_string = "Hello there, Mr bean"
print(sample_string[0])  # first character
print(sample_string[1])  # second character
print(sample_string[2])  # third character
# and so on
print(sample_string[-1])  # last character
print(sample_string[len(sample_string) - 1])  # last character
print(sample_string[-2])  # last but one item
# and so on

# print from the first to the middle characters
print(sample_string[0:len(sample_string) // 2 + 1])

# same as the above. when the starting isn't set, it sets to zero
print(sample_string[:len(sample_string) // 2 + 1])
# and when the end isn't, it is set to len(sample_string)

# same as print the whole string
print(sample_string[:])

# we have added a step to it
print(sample_string[0:len(sample_string) - 1: 2])


# List
sample_list = [1, 2, 4, 5]
print(sample_list)
print(type(sample_list))

another_list = [
    [1, 3, 5],
    [2, 4, 6],
    [-10, -20, -30]
]
print(another_list)
print(type(another_list))


# referencing and copying
some_var = "Hello"
another_var = some_var
print(some_var, another_var)

some_var = 10
print(some_var, another_var)


# this is not the same for a list
some_var_list = [1, 2, 3]
another_var_list = some_var_list
print(some_var_list, another_var_list)

some_var_list[0] = "hello"
print(some_var_list, another_var_list)

another_var_list[1] = True
print(some_var_list, another_var_list)

# list is done by reference, unlike str, int, float and bool
# to safely copy, use the indexing [:] or parse to list
new_list = [1, 2, 3]
# another_new_list = list(new_list)
another_new_list = new_list[:]
print(new_list, another_new_list)

new_list[1] = "Mango"
print(new_list, another_new_list)

another_new_list[1] = "Potato"
print(new_list, another_new_list)

# same concept of indexing applies here

new_list.append("Hi there")
print(new_list)

new_list += [False, 0.5]
print(new_list)

del (new_list[-1])  # we are removing the last element
print(new_list)

# use help(item) to find the doc on the item

# functions
rounded_pi = round(3.1415, 2)
print(rounded_pi)


# methods
sample_name = "Jessica Ann Lagman"

# convert to lower case
print(sample_name.lower())

# convert to upper case
print(sample_name.upper())

# convert to capitalize case
print(sample_name.capitalize())


# we can import numpy by doing
# import numpy as np

# sorting
some_temp_list = [2, 4, 6, 1, 0, 1]
print(sorted(some_temp_list))
print(sorted(some_temp_list, reverse=True))

# min and max
print(min(some_temp_list))
print(max(some_temp_list))

# len function
print(len(some_temp_list))
print(f"Position of 1 in the list is {some_temp_list.index(1)}")
print(some_temp_list)
some_temp_list.remove(1)
print(some_temp_list)

# reverse by reference
some_temp_list.reverse()
print(some_temp_list)


# append to the end of the list
some_temp_list.append(5)
print(some_temp_list)


# sample name, replace Lagman with Maganda-> panget (ugly)
print(sample_name.replace("Lagman", "Maganda"))
