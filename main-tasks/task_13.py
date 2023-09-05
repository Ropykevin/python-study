def email_password(email=None, password=None):
    if email is None:
        email = input("Enter your email: ")
    if password is None:
        password = input("Enter your password: ")

    if email == "admin@mail.com" and password == "Admin@123":
        result = "Login is Successful"
    else:
        result = "Invalid email or password"
        tries = 0
        while tries < 3:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == "admin@mail.com" and password == "Admin@123":
                result = "Login is Successful"
                break
            else:
                result = "Invalid email or password"
                tries += 1
        if tries == 3:
            result = "You have been blocked."
    return result

value = email_password()
print(value)
