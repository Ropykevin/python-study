from datetime import datetime

# def calculate_age(dob):
#     # Get today's date
#     today = datetime.now()

#     # Calculate the age
#     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

#     # Calculate the number of months and days
#     if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
#         months = (12 - dob.month) + today.month - 1
#         days = 31 - dob.day + today.day
#         if months == 12:
#             months = 0
#             age += 1
#     else:
#         months = today.month - dob.month
#         days = today.day - dob.day

#     return age, months, days

# # Input date of birth in YYYY-MM-DD format
# dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
# dob = datetime.strptime(dob_str, '%Y-%m-%d')

# age, months, days = calculate_age(dob)
# print(f"You are {age} years, {months} months, and {days} days old today.")

# today = datetime.now()
# birth_date = datetime(1999, 10, 20)
# years = today.year - birth_date.year
# months = today.month - birth_date.month
# days = today.day - birth_date.day
# if days < 0:
#     months -= 1
#     days += 30
# if months < 0:
#     years -= 1
#     months += 12
# print(f'You are {years} years, {months} months, and {days} days old.')

today=datetime.now()
dob=input("enter DOB(dd-mm-yyyy): ")
sdob=dob.split("-")

if len(sdob) !=3 or int(sdob[0])>31 \
    or int (sdob[1])>12 or int (sdob[2])<1900 \
    or int (sdob[2])>2023:
    print("wrong date format")
else:
    year=today.year - int(sdob[-1])
    months=today.month-int(sdob[-2])
    days=today.day-int(sdob[-3])
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        year -= 1
        months += 12
    print(f"{year} years { months} months {days} days")