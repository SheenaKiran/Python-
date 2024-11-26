# Write a Pyhton program to reverse a number

num = int(input("Enter the number: "))
org_num = num
rev = 0
while num>0:
    r = num%10
    rev = rev*10+r
    num = num//10
print(f"The the reverse of the number {org_num} is {rev}")
