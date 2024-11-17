

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            input_item = input("Enter the item to add: ").strip()
            shopping_list.append(input_item)
            print(f"{input_item} added successfully!")
            pass
        elif choice == '2':
            remove_item = input("Enter the item to remove: ").strip()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} removed successfully!")
            else:
                print("Item not found in the list.")

            # Prompt for and remove an item
            pass
        elif choice == '3':
            print("Shopping List:")
            print(f"Item(s) in the list: {shopping_list}")
           
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()