print("Simple Billing System")

item_name = input("Enter item name: ")
price = int(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Item Name:", item_name)
print("Price per item: ", price)
print("Quantity:", quantity)
print("Total Bill: ", total)
