battery = int(input("Enter battery percentage: "))

if battery >= 80:
    print("Battery Full")
elif battery >= 50:
    print("Battery Medium")
elif battery >= 20:
    print("Battery Low")
elif battery >= 0:
    print("Battery Critical")
else:
    print("Invalid battery percentage")
