#  /*Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal.
# Validates the phone number by checking if 
# it starts with +254.. or 07.. or 71… or 254.. or 01...
# Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”*/
phone_number=input("enter phone number: ")
valid=""
def phone_number_validate(phone_number=None):
    if phone_number[0:4]=="+254"and len(phone_number)==13:
        valid=(f"{phone_number} is a valid phonenumber")
    elif phone_number[0:2]==("07"or"01") and len(phone_number)==10:
        new_phone_number=phone_number[0].replace("0","+254")+phone_number[1:]
        valid =(f"The new phone number is: {new_phone_number}")
    elif phone_number[0:3]==("254") and len(phone_number)==12:
        new_phone_number="+" + phone_number
        valid =(f"The new phone number is: {new_phone_number} ")
    elif phone_number[0]==("7"or"1") and len(phone_number)==9:
        new_phone_number="+254" + phone_number
        valid =(f"The new phone number is: {new_phone_number} ")
    return valid

result=phone_number_validate()
print(result)