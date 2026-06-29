"""
Exercise 01 - Python Memory Model
"""

# Exercise 1
a = 10
b = 10

# Q1: Predict the output.
# both a and b print 10 because 1 object is refered by 2 variables

# Q2: Will id(a) and id(b) be the same? Why?
# yes the id() of a and b will be same because both the variable refer 1 object, in memory object is only at 1 poistion not on many


# ----------------------------------

# Exercise 2
a = 10
b = a
a = 20

# Q1: What is the value of a?
 # a = 20
# Q2: What is the value of b?
# b = 10
# Q3: Draw the memory diagram.

#  a ------ 10 -------b 
# b ----- 10, 20 ------ a

# ----------------------------------

# Exercise 3
city = "Delhi"

# Print:
# 1. Value

print("The value of city is :",city)

# 2. Type

print("The type of city is:", type(city))

# 3. Identity

print('The id() of city is :', id(city))

# ----------------------------------

# Exercise 4
a = 100
b = a
c = a

# How many:
# - Variables?
# there are 3 variables a,b,c

# - Objects?
# there s only 1 object which is 100

# ----------------------------------

# Exercise 5 (Theory)

# Explain in your own words:
# 1. Object - object is memory which store in the ram uniquely
# 2. Variable - variable is a lable which is help to refer or lable the objects.
# 3. Reference - reference is a connection between the variable and objects.
# 4. id() - id() refers as identity which is a unique number for the each object exist is memory