contacts = {}

# Load existing contacts
try:
    with open("contacts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 3:
                contacts[data[0]] = {
                    "phone": data[1],
                    "email": data[2]
                }
except FileNotFoundError:
    pass

while True:
    print("\n--- CONTACT MANAGER ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added.")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        with open("contacts.txt", "w") as file:
            for name, details in contacts.items():
                file.write(
                    f"{name},{details['phone']},{details['email']}\n"
                )

        print("Contacts saved. Goodbye!")
        break

    else:
        print("Invalid choice.")
