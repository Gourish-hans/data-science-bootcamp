"""
==========================================
Module 1 : Python Fundamentals
Lesson 1 : Python Memory Model
Author : Gourish Hans
==========================================
"""

# -----------------------------------------
# Example 1 : Value, Type and Identity
# -----------------------------------------

a = 10

print("Value :", a)
print("Type  :", type(a))
print("ID    :", id(a))

print("-" * 40)

# -----------------------------------------
# Example 2 : Two variables referring
#             to the same object
# -----------------------------------------

a = 10
b = 10

print("Value of a :", a)
print("Value of b :", b)

print("ID of a :", id(a))
print("ID of b :", id(b))

print("-" * 40)

# -----------------------------------------
# Example 3 : Different objects
# -----------------------------------------

a = 10
b = 20

print("ID of a :", id(a))
print("ID of b :", id(b))

print("-" * 40)

# -----------------------------------------
# Example 4 : References
# -----------------------------------------

a = 10
b = a

print("Before changing a")

print("a =", a)
print("b =", b)

print("ID of a :", id(a))
print("ID of b :", id(b))

print("-" * 20)

a = 20

print("After changing a")

print("a =", a)
print("b =", b)

print("ID of a :", id(a))
print("ID of b :", id(b))