def student_details(name, age, *subjects, **details):
    print("Name:", name)
    print("Age:", age)

    print("Subjects:")
    for s in subjects:
        print("-", s)

    print("Extra Details:")
    for key, value in details.items():
        print(f"{key}: {value}")
student_details(
    "Pranit",
    22,
    "Python", "JavaScript",
    course="Python",
    mode="Online"
)

