import math

while True:

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nWhich mathematical operation would you like to perform? \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root")

    operation = int(input("\nChoose the mathematical operation from 1 -5: "))

    if operation == 1:
        sum = float(num1 + num2)
        print(f"\nThe sum of {num1} and {num2} is {sum}.")

    elif operation == 2:
        difference = float(num2 - num1)
        print(f"\nThe difference between {num1} and {num2} is {difference}.")

    elif operation == 3:
        multiplication = float(num1 * num2)
        print(f"\nThe product of {num1} and {num2} is {multiplication}.")

    elif operation == 4:
        division = float(num1 / num2)
        print(f"\nThe quotient of {num1} and {num2} is {division}.")

    elif operation == 5:
        print(
            f"\nDo you want to find the square root of the first number ({num1}) or the second number ({num2})?\nEnter '1' for the first or '2' for the second.")
        squareroot_choice = input()

        if squareroot_choice == '1':
            if num1 < 0:
                print(f"Error: Cannot calculate the square root of a negative number")
            else:
                squareroot_result = float(math.sqrt(num1))
                print(f"The square root of {num1} is {squareroot_result}.")

        elif squareroot_choice == '2':
            if num2 < 0:
                (f"Error: Cannot calculate the square root of a negative number")
            else:
                squareroot_result = float(math.sqrt(num2))
                print(f"The square root of {num2} is {squareroot_result}.")
        else:
            print(f"\nInvalid choice for square root. Please choose either '1' for the first number or '2' for the second number.")
    else:
        print(f"\nInvalid operation choice. Please select a number between 1 and 5.")

    again = input(
        "\nDo you wish to perform any mathematical operation again? (y/n): ")
    if again != "y":
        print("Goodbye!")
        break
