#Write a Python program to find the sum of even numbers between 2 limits

l_limit = int(input("Enter the lower limit : "))
u_limit = int(input("Enter the upper limit : "))
sum = 0
if l_limit<u_limit:
    if l_limit%2 != 0:
        l_limit += 1
    else:
        l_limit += 2
    for i in range(l_limit, u_limit, 2):
        sum = sum +i
    print(f"Sum of even numbers between {l_limit} and {u_limit} is {sum}")
else:
    print("invalid input")
