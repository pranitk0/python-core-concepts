def calculate_bonus(salary):

    if salary >= 50000:
        bonus = salary * 0.10
    elif salary >= 30000:
        bonus = salary * 0.05
    else:
        bonus = 0
    return bonus

emp_salary = float(input("Enter your salary: "))

bonus_amount = calculate_bonus(emp_salary)
print("Your bonus is: ₹", bonus_amount)
