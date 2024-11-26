# Write a Python program to read number and check whether it is positive, negative or zero
num = int(input("Enter a number "))
if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is negative number")
else:
    print(f"{num} is zero")
