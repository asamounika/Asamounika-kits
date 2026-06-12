#for loop
for i in range(1,6):
    print("Hello World")

#write a python program to print the first n natural numbers?
num=int(input("Enter a number: "))
for i in range(1,num+1):
    print(i)

#to print natural numbers
num=int(input("Enter a number: "))
for i in range(num,0,-1):
    print(i)

#write a python program to print even numbers till n?
num=int(input("Enter a number: "))
for i in range(1,num+1):
    if(i%2==0):
        print(i)
print("-"*35)
for i in range(2,num+1,2):
    print(i)

#write a python program to print odd numbers from 1-n?
num=int(input("Enter a number: "))
for i in range(1,num+1):
    if(i%2!=0):
        print(i)
print("-"*35)
for i in range(1,num+1,2):
    print(i)

#write a python program to calculate sum of n natural numbers?
num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("The sum of first", num,"number is: ",sum )
