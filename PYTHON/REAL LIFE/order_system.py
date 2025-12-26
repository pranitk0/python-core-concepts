burger_price = 120
pizza_price = 250
coffee_price = 80

total = 0

print("Welcome to Online Food Order System")
print("1. Burger - ₹120")
print("2. Pizza  - ₹250")
print("3. Coffee - ₹80")

choice = input("Enter item number (1/2/3): ")
quantity = int(input("Enter quantity: "))

if choice == "1":
    total = burger_price * quantity
    print("You ordered Burger")

elif choice == "2":
    total = pizza_price * quantity
    print("You ordered Pizza")

elif choice == "3":
    total = coffee_price * quantity
    print("You ordered Coffee")

else:
    print("Invalid choice")

print("Total Bill Amount: ", total)
print("Thank you for your order!")
