def calculate_electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill
units = int(input("Enter electricity units consumed: "))
total_bill = calculate_electricity_bill(units)
print("Total Electricity Bill: ₹", total_bill)
