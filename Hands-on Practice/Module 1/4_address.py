'''
Read your name, house name, post office, district and print as follows
 	a. In different line
    b. Same line separated by comma
'''
name = input("Enter your name : ")
hname = input("Enter your house name : ")
po = input("Enter post office : ")
dist = input("Enter your district : ")
print("Your address")
print(name)
print(hname)
print(po)
print(dist)
print("Your address in single line")
print(name, hname, po, dist, sep=' ')