class mobile():
    def __init__(self,brand,price,color):
        print("Mobile market....!")
        self.brand=brand
        self.price=price
        self.color=color
def details(self):
    print(self)
m1=mobile('redmi',25000,'red')
details(m1)
m2=mobile('realme',10000,'black')
details(m2)
m3=mobile('oppo',16000,'blue')
details(m3)
print(f"brand={m1.brand}")
print(f"price={m1.price}")
print(f"color={m1.color}")
print("-------------------")
print(f"brand={m2.brand}")
print(f"price={m2.price}")
print(f"color={m2.color}")
print("--------------------")
print(f"brand={m3.brand}")
print(f"price={m3.price}")
print(f"color={m3.color}")