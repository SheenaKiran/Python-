n = int(input("Enter the number of terms : "))
f = int(input("Enter the first term: "))
d = int(input("Enter the common difference : "))
for i in range(0,n):
    print(f, end=" ")
    f = f+d
