#A Python program to read a number N and print the even numbers in reverse order starting from N

num = int(input("Enter a number : "))
for i in range(num,-1,-2):
    print(i, end=" ")
