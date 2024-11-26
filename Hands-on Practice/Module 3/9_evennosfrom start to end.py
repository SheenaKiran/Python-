#Write a Python program to print even numbers from a starting number to an ending number

start_no = int(input("Enter the starting number : "))
stop_no = int(input("Enter the stopping number : "))
if start_no<stop_no:
    if start_no%2!=0:
        start_no += 1
    for i in range(start_no, stop_no+1, 2):
        print(i, end=" ")
else:
    print("Invalid input")
