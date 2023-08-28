#if statement
temperature =0
if temperature>30:
    print("it`s warm")
    print("Drink water")
elif temperature>20:
    print("its nice")
else:
    print("its cold")
print("Done")

age =22
if age >=18:
    print("Eligible")
else:
    print("Not Eligible")

# cleaner version
age =22
if age >=18:
    message="Eligible"
else:
    message="Not Eligible"
print(message) 
    # ternary operator
message="Eligible" if age>= 18 else "Not Eligible"
print(message)

        # logical operators(they are short circuit)
        # or
        # and
        # not
# application for processing loans
high_income=True
good_credit=True
if high_income and good_credit:
    print("eligible")
else:
    print("Not eligible")
#  eligible because both are true (and neeeds both to be true for it to be true)
    # or
high_income=False
good_credit=True
if high_income or good_credit:
    print("eligible")
else:
    print("Not eligible")
    # eligible(or needs one to be true and it will be true)
# not
high_income=True
good_credit=True
student=False
if not student:
    print("eligible")
else:
    print("Not eligible")
    # eligible (not uses boolean)

high_income=True
good_credit=True
student=False

if (high_income and good_credit)and not student:
    print("eligible")
else:
    print("Not eligible")
    # eligible
# chaining comparison operators
# age shoulb be between 18 and 65
age =22
if age >=18 and age <65:
    print("eligible")
18<=age<65#in math(chaining operators)
# question
if 10=="10":
    print("a")
elif "bag">"apple"and "bag" > "cat":
    print("b")
else:
    print("c")
    # c