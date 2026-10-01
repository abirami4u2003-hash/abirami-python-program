contacts = {}

while True:
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        for name, details in contacts.items():
            print("\nName:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])

    elif choice == "5":
        with open("contacts.txt", "w") as file:
            for name, details in contacts.items():
                file.write(name + "," + details["phone"] + "," +
                           details["email"] + "\n")

        print("Contacts saved.")
        break

    else:
        print("Invalid choice.")
