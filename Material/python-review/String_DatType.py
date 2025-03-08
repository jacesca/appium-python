# ***************************** String Data Type *****************************
"""
A sequence of characters is known as string
Ex : name = "Python"
"""

# Assigning Single line string to a variable
name_1 = "Hello World"
print(name_1)

# Assigning Multi line string to a variable
name_2 ="""This is a
           Python Tutorial
           Hello 
           world
"""
print(name_2)

# Slicing - Getting the required portion of the data in the string  [1:n-1].
name_3 = name_1[1:3]
print(name_3)
name_3 = name_1[1:]
print(name_3)

# String Length -  len()
print(len(name_1))


# Convert string to upper case  - upper()
print(name_1.upper())


# Convert string to lower case  - lower()
print(name_1.lower())

# Replace some the string in sentence replace()
print(name_1.replace("World","Python"))

# String Concatenation " + "
a = "Hello"
b="World"
c=a+b
print(c)

c=a+" "+ b
print(c)


# Find the string in a sentence using Membership operators  - ( in , not in )
# If string is present in sentence then it will return "True".
name_4 = "Hey this is a python tutorial"

a= "Hey" not in name_4
print(a)
