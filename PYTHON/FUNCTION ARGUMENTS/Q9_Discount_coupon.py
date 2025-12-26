def calculate_discount(price, coupon=False):
    if coupon:
        final_price = price * 0.9  # 10% discount
    else:
        final_price = price  # no discount
    
    return final_price

amount = float(input("Enter the price: "))
use_coupon = input("Do you have a coupon? (yes/no): ").lower() == "yes"

final = calculate_discount(price=amount, coupon=use_coupon)
print(f"Final price: ₹{final}")
