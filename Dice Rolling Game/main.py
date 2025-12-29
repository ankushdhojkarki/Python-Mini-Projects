import random

def die_rolling(amount):
    result = []
    for i in range(amount):
        roll = random.randint(1,6)
        result.append(roll)
    return result

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        number = int(input("Enter the number of dice you would like to roll: "))
        dice_result = die_rolling(number)
        print(f"You rolled: {dice_result}")
    
    elif choice == 'n':
        print(f"ByeBye!")
        break

    else:
        print(f"Invalid choice! Select 'y' or 'n'")