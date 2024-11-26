password = input("Enter a password: ")
length = len(password)
if length < 6:
    print("Password strength: Weak")
elif 6 <= length <= 10:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")
