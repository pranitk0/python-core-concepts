def calculate_bill(amount, discount=0):
    final_amount = amount - discount
    return final_amount
print(calculate_bill(1000))  
print(calculate_bill(1000, discount=200))  

