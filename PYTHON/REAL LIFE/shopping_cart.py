print("Simple Shopping Cart")

items = ["Burger", "Pizza", "Tea"]
prices = [120, 250, 50]

cart = []
cart_total = 0

print("Available items:")
for idx, item in enumerate(items, start=1):
    print(f"{idx}. {item} - ₹{prices[idx-1]}")

choice = int(input("Enter item number to buy: "))   # note: input() gives text, we convert to number
quantity = int(input("Enter quantity: "))

selected_price = prices[choice - 1]
cost = selected_price * quantity

cart.append((items[choice - 1], quantity, cost))
cart_total += cost

print("\nYour cart:")
for item_name, qty, amt in cart:
    print(f"{item_name} x {qty} = ₹{amt}")

print("Total bill: ₹", cart_total)
print("Thank you for shopping!")
