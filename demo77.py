class ParkingReceipt:
    def __init__(self,Vehicle,Hours,Rate):
        self.Vehicle=Vehicle
        self.Hours=Hours
        self.Rate=Rate
    def Receipt(self):
        Fee=self.Hours*self.Rate
        print("="*50)
        print("PARKING RECEIPT")
        print("="*50)
        print(f"Vehicle Number: {self.Vehicle}")
        print(f"Hours Parked: {self.Hours}")
        print(f"Parking Fees: {Fee}")
V=input("Vehicle Number: ")
H=int(input("Hours Parked: "))
R=int(input("Rate per Hour: "))
ParkingReceipt(V,H,R).Receipt()