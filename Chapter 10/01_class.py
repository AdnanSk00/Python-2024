class Employee:
    # name = "Typing..."
    language = "Py"     # class attribute
    salary = 1200000


harry = Employee()
harry.name = "HarisAliKhan"  # instance(object) attribute
print(harry.name, harry.language, harry.salary)

shreyas = Employee()
shreyas.name = "Iyer"       # instance(object) attribute
print(shreyas.name, shreyas.salary, shreyas.language)

# Here name is object attribute, salary and language are class attribute as they directly belong to the class(Employee)