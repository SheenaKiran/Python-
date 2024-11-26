# Write a Python program to check whether a number is prime number or not

num = int(input("Enter the number: "))
flag= 0
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2,num):
        if num%i == 0:
            flag = 1
    if flag == 1:
        print(f"Number {num} is not a  prime number")
    else:
        print(f"Number {num} is a prime number")
              
