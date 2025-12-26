def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if is_valid_triangle(side1, side2, side3):
    print("The triangle is valid")
else:
    print("The triangle is not valid")
