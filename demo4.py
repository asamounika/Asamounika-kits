#write a python program to read age as input form the user and check whether the age is valid to vote or not
age=int(input("Enter your age: "))
if(age>=18):
    print("Y1ou are Elegible to vote.")
else:
    print("You are not Elegible to vote.")

#ternary operator
res="Elegible" if age>=18 else "not Elegible"
print('You are', res ,"to vote.")

#write a python program to read an integer value as input from user and check whether it is positive or negative or zero?
num=int(input("Enter a number: "))
if(num>0):
    print(f"{num} is Positive.")
elif(num<0):
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

#write a python program to read two integer values as input and find the largest number?
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if(num1>num2):
    print(f"{num1} is Greater.")
else:
    print(f"{num2} is Greater.")

#write a python program to read month number as input  from user and check whether it is valid or not?
month=int(input("Enter month number: "))
if(month>1 and month<=12):
    print(month,"is valid.")
else:
    print(month,"is invalid.")

#write a python program to read the month number as input from the user and print respective of days present in that particular month?
month=int(input("Enter month number: "))
if(month in [1,3,5,7,8,10,12]):
    print("31 days.")
elif(month in [4,6,9,11]):
    print("30 days.")
elif(month==2):
    print("28 or 29 days.")
else:
    print("Invalid month number.")

#write a python program to check whether the user enter number is even or odd?
a=int(input("Enter a number: "))
if a%2==0:
    print(f"{a} is even number.")
else:
    print(f"{a} is odd number.")

#write a python program to check whether the user entered year is a leap year or not?
year=int(input("Enter the year: "))
if(year%4==0 and year%100!=0) or (year %400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#write a python program to read 3 integer value to find largest number?
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>b and a>c:
    print(f"{a} is largest.")
elif b>a and b>c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")


#write a python program to read 3 integer value to find smallest number?
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a<b and a<c:
    print(f"{a} is smallest.")
elif b<a and b<c:
    print(f"{b} is smallest.")
else:
    print(f"{c} is smallest.")

#write a python program to read 2 integer value to find smallest number?
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a<b:
    print(f"{a} is smallest.")
else:
    print(f"{b} is smallest.")


#write a python program to read 3 integer values and find the middle number?
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if (a>b and a<c) or (a<b and a>c):
    print(f"{a} is middle.")
elif (b>a and b<c) or (b<a and b>c):
    print(f"{b} is middle.")
else:
    print(f"{c} is middle.")