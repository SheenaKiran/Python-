#Write a Python program to print the digits of a number

num = int(input("Enter the number: "))
print(f"The digits of the number {num} are")
while num>0:
    r = num%10
    print(r)
    num = num//10
