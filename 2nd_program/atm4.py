balance = 10000
transactions = 0

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            transactions += 1
            print("Deposit successful.")
            print("Updated balance: ₹", balance)
        else:
            print("Amount must be greater than zero.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Transaction failed: Insufficient balance.")
        else:
            balance = balance - amount
            transactions += 1
            print("Please collect your cash.")
            print("Updated balance: ₹", balance)

    elif choice == "4":
        print("\nTotal transactions:", transactions)
        print("Thank you for using our ATM!")
        break

    else:
        print("Please select a valid option.")
