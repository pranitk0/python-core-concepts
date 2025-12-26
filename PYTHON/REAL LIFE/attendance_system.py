print("Student Attendance System")
total_students = int(input("Enter total number of students: "))
present = 0
for i in range(total_students):
    status = input("Enter attendance (P/A): ")
    if status == "P" or status == "p":
        present = present + 1
absent = total_students - present
print("Total Students:", total_students)
print("Present Students:", present)
print("Absent Students:", absent)
