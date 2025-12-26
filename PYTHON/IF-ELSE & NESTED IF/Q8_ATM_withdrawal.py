balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw % 100 != 0:
    print("Enter amount in multiples of 100")
elif withdraw > balance:
    print("Insufficient balance")
elif balance - withdraw < 500:
    print("Minimum balance of ₹500 must be maintained")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance: ₹", balance)
