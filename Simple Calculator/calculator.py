while True:
    try:
        fnum = int(input("Enter the first number: "))
        snum = int(input("Enter the second number: "))

        print("\nWhich arithmetic operation do you want to perform?")
        print("Press '+' for addition.")
        print("Press '-' for subtraction.")
        print("Press '/' for division.")
        print("Press '*' for multiplication.\n")

        operation = input("Enter the operation you would like to perform: ")

        match operation:
            case "+":
                print(f"The sum of {fnum} and {snum} is: {fnum + snum}")
            case "-":
                print(f"The difference of {fnum} and {snum} is: {fnum - snum}")
            case "/":
                if snum == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The quotient of {fnum} and {snum} is {float(fnum / snum)}")
            case "*":
                print(f"The product of {fnum} and {snum} is: {fnum * snum}")
            case _:
                print("Invalid operation selected.")

    except Exception as e:
        print("Enter a valid value for first and second number.")

    again = input(
        "\nDo you want to perform another calculation? (yes/no): ").lower().strip()
    
    if again != ("yes", "y"):
        print("Goodbye!")
        break
