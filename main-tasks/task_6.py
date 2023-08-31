# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”.
# If the password is correct access is granted. After you show them a message , the account is blocked.
password = "admin@123"
attempts = 0
# for i in password:
#     pass_word=input("enter password: ")
#     if pass_word==password:
#         print("access is granted")
#         break    
#     attempts=attempts+1
#     if attempts<=4:
#         print("invalid password"+4-attempts +" attempts remaining")
#     else:
#         print("invalid password"+"acount blocked")
while (attempts < 4):
    # print("Enter your password:")
    pass_word = input("enter password: ")
    if (pass_word == password):
        print("Access granted.")
        break
    else:
        attempts=attempts+1
        print("Incorrect password.")
        if (attempts == 4):
            print("Your account has been blocked.")
 