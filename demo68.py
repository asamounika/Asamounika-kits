class Ticket:
    def price(self):
        print("Ticket Price: 150")
class VIPTicket(Ticket):
    def price(self):
        print("Ticket Price: 500")
cls=Ticket()
cls.price()
vip = VIPTicket()
vip.price()

