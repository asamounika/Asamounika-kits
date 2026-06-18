balance=5000
try:
    amount=int(input("Enter withdrawal amount: "))
    if amount>balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawal Successful")
except ValueError as e:
    print("Transaction Failed: ",e)