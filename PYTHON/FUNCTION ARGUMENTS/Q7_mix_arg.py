def student_report(name, age, *subjects, **details):

    print(f"Name: {name}")
    print(f"Age: {age}")
   
    if subjects:
        print("Subjects:")
        for sub in subjects:
            print("-", sub)
    else:
        print("No subjects provided")
    
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

student_report("Alice", 16, "Math", "Science", "English", grade="A", section="B", roll_no=12)
