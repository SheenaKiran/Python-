'''write a python program to Character Type Checker Accept a single character as input and
check whether it is: a vowel, a consonant, digit, or special character.'''

char = input("Enter a character : ")
if  char.isalpha():
    if char in "AEIOUaeiou":
        print(f"The entered character {char} is a vowel")
    else:
        print(f"The entered character {char} is a consonent")
elif char.isdigit():
    print(f"The entered character {char} is a digit")
else:
    print(f"The entered character {char} is a spcial character")
