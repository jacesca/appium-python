# ***************************** Set *****************************
"""
-Storing the different data type values in order and Set is changeable in run time. It doesn't allows duplicate values
-values should assign to a variable in square brackets "{} "
 Ex : name_set = {1, "python", 2.3, 4}

"""
# Create the Set
name_set ={1,2,3,"Python",1,2,3}
print(name_set)
print(type(name_set))

# We can't insert the value in set once it is created , but we can add the values.
name_set.add("World")
print(name_set)

# Length af a set
print(len(name_set))

# Remove the value from set remove() , discard() , pop()
#name_set.remove("World")
print(name_set)




# discard() method
name_set.discard("World")
print(name_set)

name_set.discard("World")
print(name_set)

# pop()
name_set.pop()
print(name_set)


# Join two sets. We need to use union() method not "+" to join two sets
a={1,2,3}
b={4,5,6,1,2,}
c=a.union(b)
print(c)

# Iterate the set using membership operator
for d in c:
    print(d)

# Find if a value is present in the set using membership operator
e = 7 in c
print(e)

# clear the data in set variable using clear() method
c.clear()
print(c)

# delete the set using del
del name_set
