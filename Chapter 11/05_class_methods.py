class Employee:
    a = 1
    # def show(self):
    #     print(f"The instance attribue of a is {self.a}")


    # If we want to print class attribue instead of instance attribue we write @classmethod above 'def show(self):'
    @classmethod
    def show(cls):
        print(f"The class attribue of a is {cls.a}")


e = Employee()
e.a = 45

# Employee.show(e)
e.show()