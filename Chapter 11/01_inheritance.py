class Student:      # Base class
    branch = "CSE"
    def show(self):
        print(f"The name of the student is {self.name} and the roll no is {self.roll}")

# class Programmer:
#     branch = "CSE and IT"
#     def show(self):
#         print(f"The name is {self.name} and the roll no is {self.roll}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Student):      # Derived class
    branch = "CSE and IT"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")



a = Student()
b = Programmer()

print(a.branch, b.branch)