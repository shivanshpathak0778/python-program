#write a class train which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under indian railways.
from random import randint

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"Train no: {self.trainNo} has {randint(0, 100)} seats available")

    def getfare(self, fro, to):
        print(
            f"Ticket fare in train no: {self.trainNo} "
            f"from {fro} to {to} is ₹{randint(222, 5555)}"
        )


t = Train(12399)

t.book("Rampur", "Jabalpur")
t.status()
t.getfare("Rampur", "Jabalpur")
