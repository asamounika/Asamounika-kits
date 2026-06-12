gtotal=0
num_pizz = int(input("Enter the number of pizzas: "))
for i in range(num_pizz):
    size = input("Enter the size of pizza (small/medium/large): ").lower()
    if size == "small":
     total = 10
    elif size == "medium":
     total = 15
    elif size == "large":
     total = 20
    else:
     print("Enter a valid size - small/medium/large")
     
     
    num_topp = int(input("Enter the number of toppings: "))
    for i in range(num_topp):
       topp = input("Enter the topping for your pizza: ").lower()
       if topp == "cheese":
        total += 2
       elif topp == "pepperoni":
        total += 3
       elif topp == "olives":
        total += 5
       elif topp == "jalapenos":
        total += 5
       else:
        print("Enter a valid topping - cheese, pepperoni, olives, jalapenos")
        break
    print(f"Your bill is ${total}")
    gtotal+=total
print(f"Your total bill is ${gtotal}")   

if gtotal<50:
  dcharge=5
else:
  dcharge=0
final_bill=gtotal + dcharge
print(f"Your final bill is ${final_bill}") 
print("Delivery charge: $",dcharge)