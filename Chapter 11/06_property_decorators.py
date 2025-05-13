class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribue of a is {cls.a}")

    @property
    def name(self):
        return f"{self.lname} {self.fname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
 
e = Employee()
e.a = 45

e.name = "Salahuddin Yusuf"
# print(e.name) 
print(e.fname,"-", e.lname)

# Employee.show(e)
e.show()