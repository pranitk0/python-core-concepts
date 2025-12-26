def calculate_grade(marks):

    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Grade F (Fail)"

marks_obtained = float(input("Enter marks: "))

grade = calculate_grade(marks_obtained)
print("Your grade is:", grade)
