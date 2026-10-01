balance = 20000

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        print("Withdrawal successful.")

while True:
    print("\n--- ATM MENU ---")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
