class RegularCustomer:
    def delivery_charge(self):
        print("Delivery Charge: 50")

class PrimeCustomer(RegularCustomer):
    def delivery_charge(self):
        print("Delivery Charge: 20")

customer = PrimeCustomer()
customer.delivery_charge()
customer = RegularCustomer()
customer.delivery_charge()