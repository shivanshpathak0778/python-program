# can you change the self parameter inside a class to somthing
# else (say "shiv") try changing self or "harry" and see the 
# effects

from random import randint

from random import randint

class Train:
    def __init__(shiv, trainNo):
        shiv.trainNo = trainNo

    def book(shiv, fro, to):
        print(f"Ticket is booked in train no: {shiv.trainNo} from {fro} to {to}")

    def status(shiv):
        print(f"Train no: {shiv.trainNo} has {randint(0, 100)} seats available")

    def getfare(shiv, fro, to):
        print(
            f"Ticket fare in train no: {shiv.trainNo} "
            f"from {fro} to {to} is ₹{randint(222, 5555)}"
        )


t = Train(12399)

t.book("Rampur", "Jabalpur")
t.status()
t.getfare("Rampur", "Jabalpur")
