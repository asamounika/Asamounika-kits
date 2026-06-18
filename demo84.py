class MembershipReceipt:
    def __init__(self,n,p,d,f):
        self.n=n
        self.p=p
        self.d=d
        self.f=f
    def Receipt(self):
        print("="*50)
        print("MEMBERSHIP RECEIPT")
        print("="*50)
        print(f"Member Name: {self.n}")
        print(f"Plan: {self.p}")
        print(f"Duration: {self.d}")
        print(f"Total Fees: {self.f}")
        print("="*50)
n=input("Member Name: ")
p=input("Plan: ")
d=input("Duration: ")
f=int(input("Monthly Fees: "))
MembershipReceipt(n,p,d,f).Receipt()