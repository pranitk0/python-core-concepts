def employee_details(id, *skills, **info):
    print("ID:", id)
    print("Skills:", skills)
    print("Info:", info)
employee_details(
    101,
    "Python",
    department="IT",
    salary=50000
)
