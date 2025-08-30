# Mini Project Shopping List Manager
shopping_list = []

while True:
    print("\nChoose your option:\n 1. Add item\n 2. Remove item\n 3. View list\n 4. Exit")
    your_choice = int(input("Enter your choice: "))

    if your_choice == 1:
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")

    elif your_choice == 2:
        item = input("Enter the item you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print(f"{item} is not in your shopping list.")

    elif your_choice == 3:
        if shopping_list:
            print("Your shopping list contains:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    elif your_choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
