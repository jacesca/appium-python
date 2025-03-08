"""
A function is a block of code which executes when we call it.
Types of function : Non-parameter function , parameter function , return type function

Using "def" keyword we will create the function.
Function name should be in camel case (First letter should be capital from 2nd word)

def functionName():
    pass

"""


# Non-parameter function
def methodOne():
    print("This is a Method one")


methodOne()


# Parameter function
def methodTwo(name):
    print("This is a ", name)


methodTwo("Python Tutorial")


#  Return type function
def sumOfTwoNumber(a, b):
    c = a + b
    return c


d = sumOfTwoNumber(10, 5)
print(d)


# Default value in function
def sumOfTwoNumber_2(a, b=10):
    c = a + b
    return c


d = sumOfTwoNumber_2(10, 20)
print(d)


# Pass list to the function
def listValue(a):
    for x in a:
        print(x)


b = [1, 2, 3, 4, 5]
listValue(b)


# Key and value as a argument
def empData(name, number, address):
    print("Name :", name)
    print("Number : ", number)
    print("Address : ", address)


empData(address="India", number=9876543210, name="Kumar")

# Arbitrary Keyword Arguments, **kwargs
"""If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition."""


def empData(**kwargs):
    print(kwargs)


empData(address="India", number=9876543210, name="Kumar")


def methodThree():
    pass
