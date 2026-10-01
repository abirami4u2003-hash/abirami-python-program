balance = 25000
pin = 4321
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Your account is locked.")
else:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Available Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Successfully deposited ₹", amount)
                print("Balance: ₹", balance)
            else:
                print("Invalid deposit.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid withdrawal.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Successfully withdrawn ₹", amount)
                print("Balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid menu choice.")
