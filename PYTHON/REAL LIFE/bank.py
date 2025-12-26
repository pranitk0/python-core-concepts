balance = 0

def check_balance():
    print(f"Current Balance: {balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"{amount} deposited successfully.")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"{amount} withdrawn successfully.")
    else:
        print("Insufficient balance!")

while True:
    print("\n--- Bank Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        amt = int(input("Enter deposit amount: "))
        deposit(amt)

    elif choice == "3":
        amt = int(input("Enter withdrawal amount: "))
        withdraw(amt)

    elif choice == "4":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice! Please try again.")
