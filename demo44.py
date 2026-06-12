slots=list(map(str,input("Enter the Booked slots: ").split()))
time_slot=input("Enter the Requested slots: ")
print("Slot Already Booked" if time_slot in slots else "Slot is Available")