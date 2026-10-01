contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact Found")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return

    print("Contact not found.")


def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(
                f"{contact['name']},{contact['phone']},{contact['email']}\n"
            )


while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        save_contacts()
        print("Contacts saved successfully.")
        break

    else:
        print("Invalid choice.")
