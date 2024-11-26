'''
Print patterns of * using nested for loop
*            * * * *           *
* *            * * *         * * *
* * *            * *       * * * * *
* * * *            *     * * * * * * *

'''
rows = int(input("Enter the numbe of rows : "))
#Pattern 1 : Right angled triangle
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
print()

#Pattern 2 : Inverted right angled triangle
for i in range(rows,0, -1):
    for k in range(rows-i):
        print("  ",end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print()

#Pattern 3 : Pyramid
for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(" ", end=" ")
    for k in range(1,2*i):
        print("*", end=" ")
    print()
