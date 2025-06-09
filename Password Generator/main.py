import string
import random

while True:
    try:
        use_letters = input("Would you like to include letters in your password? (y/n)").strip().lower()
        use_numbers = input("Would you like to include numbers in your password? (y/n)").strip().lower()
        use_symbols = input("Would you like to include symbols in your password? (y/n)").strip().lower()
        characters = ""

        if use_letters == 'y':
            characters += string.ascii_letters
        if use_numbers == 'y':
            characters += string.digits
        if use_symbols == 'y':
            characters += "!@#$%&*"
    
        if not characters:
            print("You must select atleast one character type.")
            continue 
        
        length = int(
            input("How many characters do you want in your password?"))

        if length <= 0:
            print(f"Please enter a positive number.")
            continue

        password = ""
        for i in range(length):
            password += random.choice(characters)
        print(f"Your password is: {password}\n")

        again = input(
            "Do you want to generate another password? (y/n): ").strip().lower()

        if again != 'y':
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a number.\n")
