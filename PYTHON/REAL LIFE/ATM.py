print("Welcome to Simple ATM")

balance = 10000

print("\nChoose an option:")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Your current balance is: ₹", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: ₹"))
    balance += amount
    print("Deposit successful!")
    print("Updated balance: ₹", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance: ₹", balance)
    else:
        print("Insufficient balance!")

elif choice == 4:
    print("Thank you for using the ATM!")

else:
    print("Invalid choice! Please try again.")
