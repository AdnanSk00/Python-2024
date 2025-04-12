from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"Ticket is booked for train no: {self.trainNo}\nFrom {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is fare for train no: {self.trainNo}\nFrom {fro} to {to} is Rs {randint(222, 555)}")

t = Train(72420)
t.bookTicket("Jalgaon", "Pune")
t.getStatus()
t.getFare("Jalgaon", "Pune")