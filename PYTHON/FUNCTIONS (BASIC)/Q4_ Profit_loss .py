def calculate_profit_loss(cost_price, selling_price):
    
    if selling_price > cost_price:
        profit = selling_price - cost_price
        return f"Profit of {profit}"
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        return f"Loss of {loss}"
    else:
        return "No Profit No Loss"

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))
result = calculate_profit_loss(cp, sp)
print(result)
