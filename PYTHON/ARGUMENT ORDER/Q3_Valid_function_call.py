def employee_info(emp_id, *skills, **details):
    print("ID:", emp_id)
    print("Skills:", skills)
    print("Details:", details)
employee_info(
    101,
    "Python",
    "Dsa",
    department="IT",
    experience=3
)
