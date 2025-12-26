def calculate_profit_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        return "Profit of ₹" + str(profit)
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        return "Loss of ₹" + str(loss)
    else:
        return "No Profit No Loss"

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

result = calculate_profit_loss(cp, sp)
print(result)
