balance = 15000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    while True:
        print("\n--- ATM ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            deposit = float(input("Enter deposit amount: "))

            if deposit > 0:
                balance += deposit
                print("Amount deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == 3:
            withdraw = float(input("Enter withdrawal amount: "))

            if withdraw <= 0:
                print("Invalid withdrawal amount.")
            elif withdraw > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw
                print("Please collect your cash.")

        elif choice == 4:
            print("Session ended.")
            break

        else:
            print("Invalid option.")

else:
    print("Incorrect PIN. Access denied.")
