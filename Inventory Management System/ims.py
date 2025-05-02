inventory = {}


def user():
    name = input("Enter you name: ")

    while True:
        print(
            f"\nWelcome to the Inventory Management System, {name}", "\n            \n          Menu\n")
        print("1. Add items to the inventory")
        print("2. View your inventory")
        print("3. Update item in the inventory")
        print("4. Remove item from the inventory")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            item_name = input("Enter the name of the item: ").lower()
            quantity = int(input("\nEnter the quantity of the item: "))
            price = float(input("\nEnter the price of the item: "))

            inventory[item_name] = {"quantity": quantity, "price": price}
            print(f"{item_name} has been added to the inventory.")

        elif choice == 2:
            print("\nYour Inventory: ")
            if inventory:
                for item, details in inventory.items():
                    print(
                        f"{item}: Quantity - {details['quantity']}, Price - {details['price']}")
            else:
                print(f"{name}, the inventory is empty.")

        elif choice == 3:
            item_name = input("Enter the name of the item: ").lower()
            if item_name in inventory:
                quantity = int(input("Enter the new quantity: "))
                price = float(input("Enter the new price: "))
                inventory[item_name] = {"quantity": quantity, "price": price}
                print(f"The details of item: '{item_name}' has been updated.")
            else:
                print(
                    f"Sorry {name}, the item '''{item_name}''' was not found in the inventory.")

        elif choice == 4:
            item_name = input(
                "Enter the name of the item that you want to remove: ").lower()
            if item_name in inventory:
                removed = inventory.pop(item_name, None)
                print(f"{item_name} removed from the inventory.")
            else:
                print(f"{item_name} not found in the inventory.")

        elif choice == 5:
            print(f"Goodbye {name}!")
            break


user()
