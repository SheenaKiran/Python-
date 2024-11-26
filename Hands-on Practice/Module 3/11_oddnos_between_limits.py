#Write a Python program to print odd numbers between lower limit and upper limt


l_limit = int(input("Enter the lower limit : "))
u_limit = int(input("Enter the upper limit : "))
if l_limit<u_limit:
    if l_limit%2==0:
        l_limit  += 1
    else:
        l_limit += 2
    for i in range(l_limit, u_limit, 2):
        print(i, end=" ")
else:
    print("invalid input")

