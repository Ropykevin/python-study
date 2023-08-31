email = input("Enter your email: ")
password = input("Enter your password: ")
if email == "admin@mail.com" and password == "Admin@123":
  print("Login is Successful")
else:
  tries = 0
  while tries < 3:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == "admin@mail.com" and password == "Admin@123":
      print("Login is Successful")
      break
    else:
      tries += 1
  if tries == 3:
    print("You have been blocked.")