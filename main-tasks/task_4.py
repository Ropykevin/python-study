#    Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use logical operators to solve this.
email = input("Enter your email adress: ")
valid=""
if email.index("@")>1 and (email.index(".")<len(email)-1) and (email.index(".")>email.index("@")):
    valid=(f"{email} is a valid email")
else:
    valid=(f"{email} is not a valid email")
print(valid)
# print(email)mail
# let email = prompt("Enter your email address:");
# if (email.indexOf("@")>1 && email.indexOf(".")>2) {
#     console.log("The email address is valid.");
# } else {
#     console.log("The email address is not valid.");
# }