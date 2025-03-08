"""
What is Data type?
Type of data or value is known as data type.

In python there are 5 types of data types
1. Numbers ( integer , float and complex )
2. Strings
3. list
4. Tuple
5. Dictionary

By Using type() method we can find the type of a variable
Ex : a =5
print (type(a) )
Output as : <class 'int'>

"""
# ***************************** 1. Numbers Data Type *****************************
a = 5
b = 5.2
c = 5j

print(type(a))
print(type(b))
print(type(c))

# ***************************** 2. String Data Type *****************************
"""
A sequence of characters is known as string
Ex : name = "Python"
"""
name = "Python"
print(type(name))

# ***************************** 3. List Data Type *****************************
"""  
-Storing the different data type values in order and list is changeable in run time. It allows duplicate values
-values should assign to a variable in square brackets "[] " 
 Ex : name_list = [1, "python", 2.3, 4]

"""
name_list = [1, "python", 2.2, 1]
print(name_list)
print(type(name_list))

name_list[1] = "Hello"
print(name_list)

# ***************************** 4. Tuple Data Type *****************************
"""  
-Storing the different data type values in order and tuple is unchangeable in run time. It allows duplicate values
-values should assign to a variable in  "()"
 Ex : name_tuple = (1, "python", 2.3, 1)
"""
name_tuple = (1, "python", 2.3, 1)
print(name_tuple)
print(type(name_tuple))

# Updating the tuple which leads to an error
# name_tuple[1] ="hello"
print(name_tuple)

# ***************************** 5. Dictionary Data Type *****************************
"""  
-Dictionaries are the key and value pairs. Which are written with curly brackets. " { } "
 Ex : 

 employeeData = {
  "name": "Anil",
  "number": "9876543210",
  "DOB": 1990
}

"""
employeeData = {
  "name": "Anil",
  "number": "9876543210",
  "DOB": 1990
}

print(employeeData)
print(type(employeeData))
print(employeeData["name"])