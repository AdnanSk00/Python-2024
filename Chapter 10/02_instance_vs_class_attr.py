class Employee:
    language = "Python"     # class attribute
    salary = "80000"


harry = Employee()
harry.language = "Java"  # instance(object) attribute
print(harry.language, harry.salary)

