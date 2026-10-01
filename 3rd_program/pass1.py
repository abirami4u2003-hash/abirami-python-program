import re

password = input("Enter your password: ")

# Check password strength
if len(password) < 8:
    print("Password is too short.")
elif not re.search("[A-Z]", password):
    print("Password must contain an uppercase letter.")
elif not re.search("[a-z]", password):
    print("Password must contain a lowercase letter.")
elif not re.search("[0-9]", password):
    print("Password must contain a number.")
elif not re.search("[@#$%]", password):
    print("Password must contain a special character.")
else:
    print("Strong password.")

    # Caesar encryption
    encrypted = ""

    for char in password:
        encrypted += chr(ord(char) + 3)

    with open("password.txt", "w") as file:
        file.write(encrypted)

    print("Encrypted password stored successfully.")
