class Employee:
    def bonus(self): print("Bonus: 5000")
class Manager(Employee):
    def bonus(self): print("Bonus: 20000")
(Manager() if input().strip() == "Manager" else Employee()).bonus()