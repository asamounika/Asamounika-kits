class RechargeReceipt:
    def __init__(self,name,mobile,plan,amount):
        self.name=name
        self.mobile=mobile
        self.plan=plan
        self.amount=amount
    def Receipt(self):
        print("="*50)
        print("RECHARGE RECEIPT")
        print("="*50)
        print(f"Customer Name: {self.name}")
        print(f"Plan Selected: {self.plan}")
        print(f"Amount Paid: {self.amount}")
        print("SUCCESSFUL")
name=input("Name: ")
mobile=int(input("Mobile: "))
plan=input("Plan: ")
amount=int(input("Amount: "))
RechargeReceipt(name,mobile,plan,amount).Receipt()