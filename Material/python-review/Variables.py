"""
What is a variable?
Variables are containers for storing values.
We can store any data values in python variable
In python no need to declare any command to create a variable.
A variable is created the moment you first assign a value to it.

Python variables Rules
=========================
A variable name must start with a letter or the underscore character ( a = 5 or _name = "python" or name = "python" )
A variable name cannot start with a number (1_a = 5 or 1name ="python" )
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )   (name_1 = "python)
Variable names are case-sensitive (name, Name and NAME are three different variables)

"""
a = 5
a = "python"
b = 5.2
print(a)

name = "Python"
Name = "Hello"

# Assign single value to Multiple Variables
a = b = c = 3

print(a)
print(b)
print(c)

# Assign multiple values to Multiple Variables in single line
a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
