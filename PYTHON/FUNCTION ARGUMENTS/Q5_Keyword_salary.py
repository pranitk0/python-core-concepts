def calculate_salary(base, **components):
    total = base
    print(f"Base Salary: {base}")
    
    for key, value in components.items():
        total += value
        print(f"{key}: {value}")
    
    print(f"Total Salary: ₹{total}")
    return total
calculate_salary(30000, bonus=5000, hra=2000, allowances=1000)
