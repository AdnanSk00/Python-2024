class Employee:
    language = "Python"
    salary = "80000"

    def getInfo(objHarry):
        print(f"The language is {objHarry.language}. The salary is {objHarry.salary}")

    # def greet(self):
        # print("Good Morning!")
    
    # If I dont want to pass self in greet() I will write @staticmethod above the 'def greet():'
    @staticmethod
    def greet():    
        print("Good Morning!")


harry = Employee()
# harry.language = "Java"

harry.getInfo()
# Employee.getInfo(harry) 
# Note: Above both are same

harry.greet()
