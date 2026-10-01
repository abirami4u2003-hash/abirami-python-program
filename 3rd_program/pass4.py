password = input("Enter your password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters.")
else:
    if (any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(not c.isalnum() for c in password)):

        # Reverse the password
        encrypted = password[::-1]

        with open("password_data.txt", "w") as file:
            file.write(encrypted)

        print("Password strength: Strong")
        print("Encrypted data saved successfully.")

    else:
        print("Password strength: Weak")
        print("Use uppercase, lowercase, digit and special character.")
