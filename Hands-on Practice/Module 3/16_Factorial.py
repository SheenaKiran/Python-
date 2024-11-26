# Input: Take the value from the user
num = int(input("Enter a positive integer: "))

# Initialize the factorial result
factorial = 1

# Using a while loop to calculate factorial directly with num
while num > 1:
    factorial *= num
    num -= 1
print(f"The factorial is {factorial}.")
