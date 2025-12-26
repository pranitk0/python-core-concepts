def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not any(char.isupper() for char in password):
        return "Weak"
    if not any(char.islower() for char in password):
        return "Weak"
    if not any(char.isdigit() for char in password):
        return "Weak"
    if not any(char in "!@#$%^&*" for char in password):
        return "Weak"
    return "Strong"

pwd = input("Enter your password: ")

strength = check_password_strength(pwd)
print("Password strength:", strength)
