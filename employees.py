employeenames = []

class Employees:
    def __init__(self, FirstName, LastName, EmployeeID):
        self.__FirstName = FirstName                                    #string
        self.__LastName = LastName                                      #string
        self.__FullName = FirstName + " " + LastName                    #string
        self.__Email = FirstName + "." + LastName + "@company.com"      #string
        self.__EmployeeID = EmployeeID                                  #string

    def GetEmployeeEmail(self):
        return self.__EmployeeID, self.__Email
    
    def PrintDetails(self):
        print("Employee ID, First Name, Last Name, FullName and Email")
        return self.__EmployeeID, self.__FirstName, self.__LastName, self.__FullName, self.__Email

try:
    with open("employees.txt") as f:
        for i in range(0, 27, 3):
            FirstName = f.readline().strip()
            LastName = f.readline().strip()
            EmployeeID = f.readline().strip()
            employeenames.append(Employees(FirstName, LastName, EmployeeID))
except FileNotFoundError:
    print("File not found.")

for i in range(len(employeenames)):
    print(Employees.GetEmployeeEmail(employeenames[i]))
    
for i in range(len(employeenames)):
    print(Employees.PrintDetails(employeenames[i]))
