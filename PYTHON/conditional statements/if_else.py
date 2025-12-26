def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(10))        
print(even_or_odd(3))

#Q2

def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
age = int(input("Enter your age: "))
result = check_voting_eligibility(age)
print(result)

#Q3
def grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 80:
        return "Grade B"
    elif marks >= 70:
        return "Grade C"
    elif marks >= 60:
        return "Grade D"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))
result = grade(marks)
print(result)

#Q4

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = largest_of_three(num1, num2, num3)

print("The largest number is:", result)

#Q5
def is_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"
year = int(input("Enter a year: "))
result = is_leap_year(year)
print(result)

#Q6

def profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        return "Profit"
    elif selling_price < cost_price:
        return "Loss"
    else:
        return "No Profit No Loss"
cost = float(input("Enter the Cost Price: "))
selling = float(input("Enter the Selling Price: "))
result = profit_or_loss(cost, selling)

print(result)

#Q7

def triangle_valid(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Valid Triangle"
    else:
        return "Not a Valid Triangle"
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
result = triangle_valid(side1, side2, side3)

print(result)

#Q8

def calculate_salary_with_bonus(salary, years_of_service):
    if years_of_service >= 5:
        bonus = 0.10 * salary
        final_salary = salary + bonus
        return "Final Salary after 10% bonus: final_salary"
    else:
        return "Final Salary (No bonus): salary"
salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))
result = calculate_salary_with_bonus(salary, years)

print(result)

#Q9

def calculate_electricity_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return units * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10
units = float(input("Enter units consumed: "))
print("Total Electricity Bill: ", calculate_electricity_bill(units))

#Q10
def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
result = simple_calculator(number1, number2, op)
print("Result:", result)



