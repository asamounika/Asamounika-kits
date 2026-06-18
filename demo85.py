class TransactionReceipt:
    def __init__(self,name,balence,transfer_amount):
        self.name=name
        self.balence=balence
        self.tranfer_amount=transfer_amount
    def Receipt(self):
        camt=self.balence-self.tranfer_amount
        print("="*50)
        print("TRANSACTION RECEIPT")
        print("="*50)
        print(f"User Name: {self.name}")
        print(f"Opening Amount: {self.balence}")
        print(f"Tranfer Amount: {self.tranfer_amount}")
        print(f"Current Amount: {camt}")
        print("status: SUCCESSFULL")
        print("="*50)
name=input("User: ")
balence=int(input("Wallet Balance: "))
transfer_amount=int(input("Transfer Amount: "))
TransactionReceipt(name,balence,transfer_amount).Receipt()