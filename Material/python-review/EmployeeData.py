class EmployeeDetails:
    _company = "xyz"

    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.addr = address

    def empDetails(self, name, number, address):
        print("Name :", name)
        print("Number : ", number)
        print("Address : ", address)

    def empName(self):
        print("Employee Name is : ", self.name)

    def empCompany(self):
        print("This is a company :",self._company)




emp = EmployeeDetails("Kumar", 9876543210, "India")

#emp.empDetails("Anil", 9876543210, "Hyd")

#emp.empName()

