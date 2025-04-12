class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    

p = Programmer("Vaniya Agrawal", 130000, 425001)
print(p.company, p.name, p.salary, p.pin)

q = Programmer("Ibtihal Aboussad", 120000, 425002)
print(q.company, q.name, q.salary, q.pin)

r = Programmer("Adnan Shaikh", 900000, 425003)
print(r.company, r.name, r.salary, r.pin)
