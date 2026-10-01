contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Show All")
    print("5. Save and Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print(contact)
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "4":
        for contact in contacts:
            print(contact)

    elif choice == "5":
        with open("contacts.txt", "w") as file:
            for contact in contacts:
                file.write(
                    contact["name"] + "|" +
                    contact["phone"] + "|" +
                    contact["email"] + "\n"
                )

        print("Data saved successfully.")
        break

    else:
        print("Invalid choice.")
