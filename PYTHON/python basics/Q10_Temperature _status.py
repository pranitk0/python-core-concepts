temp = float(input("Enter temperature in °C: "))

if temp < 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Normal")
else:
    print("Hot")
