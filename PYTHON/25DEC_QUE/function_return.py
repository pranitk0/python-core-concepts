def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"
print(calculate(10, 5, "+"))   
print(calculate(10, 5, "-"))   
print(calculate(10, 5, "*"))   
print(calculate(10, 5, "/"))   
print(calculate(10, 5, "%"))