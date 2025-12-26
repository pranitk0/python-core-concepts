def login_system(**credentials):
    correct_username = "admin"
    correct_password = "12345"
    
    username = credentials.get("username")
    password = credentials.get("password")
    
    if username == correct_username and password == correct_password:
        return "Login Successful"
    else:
        return "Login Failed "

result = login_system(username="admin", password="12345")
print(result)
