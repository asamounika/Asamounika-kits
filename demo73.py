class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def bill(self, emp):
        total = sum(i.price for i in self.items)
        print("=" * 50)
        print("CORPORATE CAFETERIA BILL")
        print("=" * 50)
        print(f"\nEmployee ID   : {emp.eid}")
        print(f"Employee Name : {emp.name}\n")
        print("-" * 50)
        print("Item  Price")
        print("-" * 50)
        for i in self.items:
            print(f"{i.name}  Rs.{i.price}")
        print("-" * 50)
        print(f"\nTotal Amount  : Rs.{total}")
        print("\nPayment Status : PAID")
        print("=" * 50)
emp = Employee("23JR07", "Chinnari")
order = Order()
emp = Employee("23JR08", "Chinnu")
order = Order()
order.add_item(FoodItem("Coffee", 40))
order.add_item(FoodItem("Sandwich", 80))
order.add_item(FoodItem("Brownie", 60))
order.bill(emp)
