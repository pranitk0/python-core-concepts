def print_student_details(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
print_student_details(
    name="Pranit",
    age=20,
    course="Python",
    marks=85
)
