class Employee:     # Base class
    company = "Infosys"
    name = "Default name"
    salary = "1.2L"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class coder:        # Base class
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, coder):      # Derived class
    company = "Infosys Springboard"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")



a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()