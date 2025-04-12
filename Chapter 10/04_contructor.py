class Employee:
    language = "Python"
    salary = 90000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def __init__(self, name, salary, language): # dunder method automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    @staticmethod
    def greet():    
        print("Good Morning!")


# harry = Employee()
# harry.name = "Saquib"
# print(harry.name, harry.salary)

asim = Employee("Saquib", 70000, "JavaScript")
print(asim.name, asim.salary, asim.language)



# harry.getInfo()
# Employee.getInfo(harry) 
# Note: Above both are same


