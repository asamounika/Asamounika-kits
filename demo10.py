#program1
def one():
    def two():
        print("two")
    print("One")
one()

#program2
def washhands():
    print("Washing hands")
def servefood():
    print("Serving food")
def eatfood():
    washhands()
    servefood()
    print("Eating food")
    washhands()
eatfood()

#program3
def one(xyz):
    print("First Function "+xyz())
def two():
    return "Second Function"
one(two)

#program4 ananymous function or lambda function
def add(a,b):
    return a+b
print(add(5,3))

add=lambda a,b:a+b
print(add(5,3))