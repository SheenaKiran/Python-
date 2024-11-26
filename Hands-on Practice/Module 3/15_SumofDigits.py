#Write a Python program to sum of digits of a number

num = int(input("Enter the number: "))
sum = 0
while num>0:
    r = num%10
    sum = sum+r
    num = num//10
print(f"The sum of digits of the number {num} is {sum}")