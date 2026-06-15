class HotelInvoice:
    def __init__(self,name,room,nights):
        self.name=name
        self.room=room
        self.nights=nights
    def Receipt(self):
        roomRate=3500
        total=roomRate*self.nights
        print("="*50)
        print("HOTEL INVOICE")
        print("="*50)
        print(f"Guest Name: {self.name}")
        print(f"Room Type: {self.room}")
        print(f"Nights Stays: {self.nights}")
        print(f"Total Amount: {total}")
name=input("Name: ")
room=input("Room Type: ")
nights=int(input("Nights Stayed: "))
HotelInvoice(name,room,nights).Receipt()