class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square = {self.n*self.n}")

    def qube(self):
        print(f"Qube = {self.n*self.n*self.n}")

    def sqrRoot(self):
        print(f"Square root = {self.n**0.5}")


a = Calculator(9)
a.square()
a.qube()
a.sqrRoot()
