import json

filename = "contacts.json"

# Load contacts
try:
    with open(filename, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []


while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        contact = {
            "name": input("Enter name: "),
            "phone": input("Enter phone: "),
            "email": input("Enter email: ")
        }

        contacts.append(contact)

        with open(filename, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact added successfully.")

    elif choice == "2":

        name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "3":

        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)

                with open(filename, "w") as file:
                    json.dump(contacts, file, indent=4)

                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "4":

        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for contact in contacts:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "5":

        with open(filename, "w") as file:
            json.dump(contacts, file, indent=4)

        print("All contacts saved.")
        break

    else:
        print("Invalid choice.")
