password = input("Enter password: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:

    key = 7
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) ^ key)

    with open("secure_data.txt", "w") as file:
        file.write(encrypted)

    print("Strong password.")
    print("Password encrypted and stored successfully.")

else:
    print("Weak password.")
