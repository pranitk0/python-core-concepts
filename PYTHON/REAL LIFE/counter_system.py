print("Counter System")

count = 0  

choice = input("Type '+' to increase or '-' to decrease: ")

if choice == "+":
    count = count + 1
    print("Counter increased")
    print("Value:", count)

elif choice == "-":
    count = count - 1
    print("Counter decreased")
    print("Value:", count)

else:
    print("Invalid input")
