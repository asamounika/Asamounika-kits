#write a python program to print the factorial of n?
num=int(input("Enter a number: "))
fact=1
for i in  range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is:",fact)

#write a python program to print multiplication table of n?
num=int(input("Enter a number: "))
print(f"Multiplication table of {num}: ")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#write a python program to print reversed multiplication table?
num=int(input("Enter a number: "))
print(f"Multiplication table of {num}: ")
for i in range(10,0,-1):
    print(f"{num} x {i} = {num*i}")

#write a program to print multiplication tables from 1-n?
num=int(input("Enter a number: "))
for i in range(1,num+1):
    print(f"Multiplication table of {i}: ")
    print("----------------------------------")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
        
#write a program to print multiplication of table from n-1?
num=int(input("Enter a number: "))
for i in range(num,0,-1):
    print(f"Multiplication table of {i} ")
    print("----------------------------------")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
