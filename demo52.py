class Vehicle:
    def __init__(self,b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print('Vehicle class Constructor')
class Bike(Vehicle):
    def __init__(self, b, p, c, s,g,m):
        super().__init__(b, p, c, s)
        self.g=g
        self.m=m
        print('Bike class Constructor')
b1=Bike('Tata',25000,'black',2,3,45)