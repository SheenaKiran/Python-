# Write a Python program to print the amstrong numbers between 2 limits

low = int(input("Enter the lower limit : "))
up = int(input("Enter the upperr limit : "))
for num in range(low+1, up):
    org_num = num
    sum=0
    while num>0:
        r = num%10
        sum = sum+r**3
        num = num // 10
    if org_num == sum:
        print(org_num)
        
