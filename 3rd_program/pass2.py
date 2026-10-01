password = input("Enter password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:

    encrypted = ""

    for ch in password:
        encrypted += chr((ord(ch) + 5) % 127)

    file = open("encrypted_password.txt", "w")
    file.write(encrypted)
    file.close()

    print("Password is strong.")
    print("Encrypted password saved to file.")

else:
    print("Weak password.")
    print("Use at least 8 characters with uppercase, lowercase, number and special character.")
