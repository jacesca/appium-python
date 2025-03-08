# The process adding extra functionality to the existing code for a function is called decorator
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

def logData(func):
    def inner_func(x):
        print("****************************************")
        print("Strating of a function : ", func.__name__)
        a = func(x)
        print(a)
        print("Ending of a function : ", func.__name__)
        print("****************************************")
    return inner_func


@logData
def sumOfNumbers(a):
    return a + 5


sumOfNumbers(10)
