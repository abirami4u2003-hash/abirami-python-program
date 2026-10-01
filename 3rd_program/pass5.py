import base64

while True:
    print("\n===== PASSWORD SECURITY SYSTEM =====")
    print("1. Create Password")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        password = input("Enter password: ")

        score = 0

        if len(password) >= 8:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score == 5:
            print("Password strength: Very Strong")

            # Base64 encoding
            encrypted = base64.b64encode(
                password.encode()
            ).decode()

            with open("password.txt", "w") as file:
                file.write(encrypted)

            print("Encoded password saved successfully.")

        elif score >= 3:
            print("Password strength: Medium")
            print("Please improve your password.")

        else:
            print("Password strength: Weak")

    elif choice == "2":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
