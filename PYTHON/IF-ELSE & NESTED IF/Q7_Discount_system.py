amount = float(input("Enter amount: "))

if amount >= 1000:
    if amount >= 5000:
        discount = amount * 0.20
    else:
        if amount >= 3000:
            discount = amount * 0.10
        else:
            discount = amount * 0.05
else:
    discount = 0

print("Final Amount:", amount - discount)
