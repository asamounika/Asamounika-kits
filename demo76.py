class BoardingPass:
    def __init__(self,name,flight,Seat):
        self.name=name
        self.flight=flight
        self.Seat=Seat
    def Receipt(self):
        print("="*50)
        print("BOARDING PASS")
        print("="*50)
        print(f"Passenger Name: {self.name}")
        print(f"Flight number: {self.flight}")
        print(f"Seat Number: {self.Seat}")
        print("Status: CHECK-IN COMPLETE\n")
        print("="*50)
name=input("Passenger: ")
flight=input("Flight Number: ")
Seat=input("Seat Number: ")
bp=BoardingPass(name,flight,Seat)
bp.Receipt()