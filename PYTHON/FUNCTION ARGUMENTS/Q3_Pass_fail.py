def check_pass_fail(marks, passing_marks=40):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"

score = float(input("Enter marks obtained: "))

result = check_pass_fail(score)
print("Result:", result)
