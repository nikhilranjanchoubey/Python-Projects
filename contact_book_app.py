# Empty dictionary to store contacts
contacts = {}

while True:
    print("\n===== Contact Book App =====")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice = ")

    # Create Contact
    if choice == "1":
        name = input("Enter your name = ")

        if name in contacts:
            print(f"Contact name '{name}' already exists!")
        else:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")

            contacts[name] = {
                "age": int(age),
                "email": email,
                "mobile": mobile
            }

            print(f"Contact '{name}' has been created successfully!")

    # View Contact
    elif choice == "2":
        name = input("Enter contact name to view = ")

        if name in contacts:
            contact = contacts[name]

            print("\nContact Details")
            print(f"Name   : {name}")
            print(f"Age    : {contact['age']}")
            print(f"Email  : {contact['email']}")
            print(f"Mobile : {contact['mobile']}")
        else:
            print("Contact not found!")

    # Update Contact
    elif choice == "3":
        name = input("Enter name to update contact = ")

        if name in contacts:
            age = input("Enter updated age = ")
            email = input("Enter updated email = ")
            mobile = input("Enter updated mobile number = ")

            contacts[name] = {
                "age": int(age),
                "email": email,
                "mobile": mobile
            }

            print(f"Contact '{name}' updated successfully!")
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == "4":
        name = input("Enter contact name to delete = ")

        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' has been deleted successfully!")
        else:
            print("Contact not found!")

    # Search Contact
    elif choice == "5":
        search_name = input("Enter contact name to search = ")
        found = False

        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(
                    f"Found -> Name: {name}, "
                    f"Age: {contact['age']}, "
                    f"Mobile: {contact['mobile']}, "
                    f"Email: {contact['email']}"
                )
                found = True

        if not found:
            print("No contact found with that name!")

    # Count Contacts
    elif choice == "6":
        print(f"Total contacts in your book : {len(contacts)}")

    # Exit
    elif choice == "7":
        print("Good Bye... Closing the program")
        break

    else:
        print("Invalid Choice! Please try again.")