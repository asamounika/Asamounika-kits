class Student:
    def __init__(self,name,age):
        print("Product object is created..!")
        self.name=name
        self.age=age
def details(self):
    print("------------")
    print(f"name is {self.name}")
    print(f"age is {self.age}")
s1=Student('scott',23)
details(s1)
s2=Student('allen',24)
details(s2)    
