class ClintInvoice:
    def __init__(self,client,project,hours,hrate):
        self.client=client
        self.project=project
        self.hours=hours
        self.hrate=hrate
    def Receipt(self):
        Amt=self.hours*self.hrate
        print("="*50)
        print("CLIENT INVOICE")
        print("="*50)
        print(f"Client Name: {self.client}")
        print(f"Project Name: {self.project}")
        print(f"Hours Worked: {self.hours}")
        print(f"Total Amount: {Amt}")
        print("="*50)
client=input("Client: ")
project=input("Project: ")
hours=int(input("Hours Worked: "))
hrate=int(input("Hourly Rate: "))
ClintInvoice(client,project,hours,hrate).Receipt()