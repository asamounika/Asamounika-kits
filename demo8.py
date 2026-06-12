#Write a python program to check whether the user entered integer is a prime number or not?
num=int(input("Enter a number: "))
if num<1:
    print(num,"is not a prime number.")
else:
    for i in range(2,num):
        if num % i ==0:
            print(num,"is not  a prime number.")
            break
        else:
            print(num,"is a prime number.")

#Write a python program to print the reverse integer of user entered number without using built in functions?
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#Write a python program to check whether the user entered integer is a palindrome or not?
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number.")