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

# Create a Dictionary
employeeData={"name":"Anil","number":987654310,"DOB":1990}
print(employeeData)
print(type(employeeData))

# Access the value from dictionary
a=employeeData["number"]
print(a)

# Update or change the value
employeeData["name"] ="Kumar"
print(employeeData)

# Add key and value for existing dictionary
employeeData["address"]="India"
print(employeeData)

# length of a dictionary
print(len(employeeData))

# Copy the dictionary to other variable
emp = employeeData.copy()
print(emp)

# Iterate the values in dictionary
for a in employeeData.keys():
    print(employeeData[a])

# Iterate both keys and values
for a,b in employeeData.items():
    print(a,b)

# Remove the value
employeeData.pop("address")
print(employeeData)

# Clear the dictionary
employeeData.clear()
print(employeeData)

# delete the dictionary
del employeeData
#print(employeeData)
