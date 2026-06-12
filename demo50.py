class Customer:
    def __init__(self):
        pass
    #Mutator or setter Method
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def set_age(self,age):
        self.age=age
    #Accessor or Getter Method
    def get_id(self):
        print(f"Id is {self.id}")
    def get_name(self):
        print(f"Name is {self.name}")
    def get_age(self):
        print(f"Age is {self.age}")
    