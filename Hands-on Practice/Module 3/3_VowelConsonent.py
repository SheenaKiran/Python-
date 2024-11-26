char = input("Enter a single character: ")

if char.isalpha():            # Check if the input is a single alphabetic character
    if char in 'AEIOUaeiou':  # Check if the character is a vowel
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input.")