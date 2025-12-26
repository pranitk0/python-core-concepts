#Q1 
def  add_numbers(a, b, /):
    return a + b 
result = add_numbers(5,5)
print(result)

#Q2
def max_of_three(a, b, c, /):
    return max (a,b,c)
result= max_of_three(10,5,33)
print(result)

#Q3
def student_info(* ,name, age, course):
    print("my name is ",name)
    print("my age is",age)
    print("course type",course)
student_info(name="pranit",age="11",course="python") 

#Q4
def calculate_salary(* ,basic, bonus):
    return basic + bonus
total= calculate_salary(basic=10000,bonus=1000)
print(total)
    
#Q5
def calculate_bill(units, *, rate):
    return units * rate
total= calculate_bill(100, rate=5)
print(total)

#Q6
def book_ticket(movie,* ,seats=1):
    print("movie name: ",movie)
    print("seats: ",seats)
book_ticket("dhurandhar",seats=5)

#Q7
def even(num):
    return num % 2==0 
print(even(4))    
print(even(5))

#Q8 
def check_login(*, username, password):
    correct_username = "admin"
    correct_password = "1234"
    
    if username == correct_username and password == correct_password:
        return "Login Successful"
    else:
        return "Login Failed"
print(check_login(username="admin",password=1234))        

#Q9
def discount(price, *, coupon=False):
    if coupon:
        return price * 0.9 
    else:
        return price
print(discount(200))           
print(discount(200,coupon=False))

#Q10
def employee_details(id, name, department):
    return f"id:{id},name:{name},department:{department}"
details1=employee_details(101,"pranit","comp")
details2=employee_details(id=102,name="raj",department="IT")
print(details1)
print(details2)
    


















