#Write a Python program to find the  even numbers from lower limit to upper limit


l_limit = int(input("Enter the lower limit : "))
u_limit = int(input("Enter the upper limit : "))
sum = 0
if l_limit < u_limit:
    if l_limit%2!=0:
        l_limit +=1
    for i in range(l_limit, u_limit+1, 2):
        sum += i
    print("Sum ",sum)
else:
    print("Invalid input")
