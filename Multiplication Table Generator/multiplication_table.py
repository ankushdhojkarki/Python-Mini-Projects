# Takes a number as user input and returns a multiplication table of that number.


while True:

    try:
        user_input = int(input("\nEnter a number: "))

        for i in range(1,11):
            print(f"\n{user_input} * {i} = {user_input * i}")

    except ValueError:
        print("Please enter a valid number.")      

    ask = input("\nDo you want to get multiplication table of any other number? [y/n] ").lower()

    if ask != 'y'.lower():
        print("Goodbye!")
        break