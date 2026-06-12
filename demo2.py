#Arthmetic operators
x=13
y=7
print(f"Addition of x & y is {x+y}")
print(f"Substraction of x & y is {x-y}")
print(f"Multiplication of x & y is {x*y}")
print(f"Division of x & y is {x/y}")
print(f"Modulo Division of x & y is {x%y}")
print(f"Positive Floor Divvision of x & y is {x//y}")
print(f"Negative Floor Division of x & y is {-x//y}")
print(f"Exponential of x & y is {x**y}")

#Relational operators
x=13
y=7
print(f"Less Than of x & y is {x<y}")
print(f"Greater than of x & y is {x>y}")
print(f"Less Than or Equal To of x & y is {x<=y}")
print(f"greater Than or Equal to of x & y is {x>=y}")
print(f"Equal to of x & y is {x==y}")
print(f"Not Equal of x & y is {x!=y}")

#Assignment operators
num=10
print(f"num= {num}")
num+=2 #num=num+2
print(f"num={num}")
num-=4
print(f"num={num}")
num*=3
print(f"num={num}")
num%=5
print(f"num={num}")
num//=6
print(f"num={num}")
num**=2
print(f"num={num}")

#Logical operators
num=10
print(num>5 and num<15)
print(num>5 or num<5)
print(not(num<15))

#Bitwise operators
a=10 #0000 1010
b=15 #0000 1111
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
print('a<<2=',a<<2)
print('a>>2=',a>>2)
print('~a=',~a)

#Membership operators
#in & not in
List=[10,30,25,40,15,20]
print(10 in List)
print(50 in List)
print(10 not in List)
print(50 not in List)
print("Python" in 'i am working on python')
print("Python" in 'i am working on Python')

#Identity operators
num1=10
print(num1)
print(id(num1))
num2=20
print(num2)
print(id(num2))
num3='10'
print(num3)
print(id(num3))
num4=10
print(num4)
print(id(num4))
print(num1 is  num4)