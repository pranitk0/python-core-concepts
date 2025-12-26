def student_info(name, age, **details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print("No additional details provided.")

student_info("Pranit", 20, roll_no=101, course="Python", grade="A")
