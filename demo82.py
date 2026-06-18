class ServiceReceipt:
    def __init__(self,owner,petname,service,charge):
        self.owner=owner
        self.petname=petname
        self.service=service
        self.charge=charge
    def Receipt(self):
        print("="*50)
        print("SERVICE RECEIPT")
        print("="*50)
        print(f"Owner Name: {self.owner}")
        print(f"Pet Name: {self.petname}")
        print(f"Service: {self.service}")
        print(f"Amount: {self.charge}")
        print("="*50)
owner=input("Owner Name: ")
petname=input("Pet Name: ")
service=input("Service: ")
charge=int(input("Charge: "))
ServiceReceipt(owner,petname,service,charge).Receipt()