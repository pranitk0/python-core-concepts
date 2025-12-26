a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is the largest number")
elif b >= a and b >= c:
    print("B is the largest number")
else:
    print("C is the largest number")
